"""Generate the state-level demographics CSV used by the app.

Output schema: State | Year | Total Population | Median Household Income | State Abbrev

Data comes from the American Community Survey 1-year Estimates, retrieved from the
US Census Bureau's API via the *censusdis* package.
"""

from __future__ import annotations

from pathlib import Path

import us
from censusdis.datasets import ACS1
from censusdis.multiyear import download_multiyear

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OUTPUT_FILE = Path(__file__).parent / "state_data.csv"

CENSUS_VARS: dict[str, str] = {
    "NAME": "State",
    "B01001_001E": "Total Population",
    "B19013_001E": "Median Household Income",
}

# Data was not published in 2020 due to Covid-19.
# See https://www.census.gov/programs-surveys/acs/data/experimental-data.html
YEARS: list[int] = [year for year in range(2005, 2024) if year != 2020]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_state_abbrev(state_name: str) -> str | None:
    """Return the two-letter postal abbreviation for *state_name*.

    Returns ``None`` for territories such as Puerto Rico that lack an
    abbreviation in the *us* package.
    """
    match us.states.lookup(state_name):
        case None:
            return None
        case state:
            return state.abbr


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    df = download_multiyear(
        dataset=ACS1,
        vintages=YEARS,
        download_variables=list(CENSUS_VARS),
        state="*",
        rename_vars=False,
        prompt=False,
    )
    df = df.rename(columns=CENSUS_VARS)

    # Reorder columns so State and Year come first.
    leading = ["State", "Year"]
    remaining = [col for col in df.columns if col not in leading]
    df = df[leading + remaining]

    df = df.sort_values(["State", "Year"])
    df["State Abbrev"] = df["State"].apply(get_state_abbrev)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Wrote {len(df):,} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()


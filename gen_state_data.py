"""
This script generates the dataset which is used by the app. The final structure of the data looks like:
(State, Year, Total Population, Median Household Income, State Abbrev)

Data comes from the American Community Survey 1-year Estimates, and is retrieved from the US Census Bureau's
API via the censusdis package.
"""

from __future__ import annotations

import us
from censusdis.datasets import ACS1
from censusdis.multiyear import download_multiyear

CENSUS_VARS: dict[str, str] = {
    "NAME": "State",
    "B01001_001E": "Total Population",
    "B19013_001E": "Median Household Income",
}

# Note that data was not published in 2020 due to Covid-19.
# See https://www.census.gov/programs-surveys/acs/data/experimental-data.html
YEARS: list[int] = [year for year in range(2005, 2024) if year != 2020]

OUTPUT_FILE = "state_data.csv"


def get_abbrev(state_name: str) -> str | None:
    """Return the two-letter abbreviation for *state_name*, or None for territories."""
    match = us.states.lookup(state_name)
    return match.abbr if match else None  # Happens for Puerto Rico


def main() -> None:
    df = download_multiyear(
        dataset=ACS1,
        vintages=YEARS,
        download_variables=CENSUS_VARS.keys(),
        state="*",
        rename_vars=False,
        prompt=False,
    )
    df = df.rename(columns=CENSUS_VARS)

    # Reorder columns so State and Year come first
    cols = df.columns.tolist()
    new_order = ["State", "Year"] + [col for col in cols if col not in {"State", "Year"}]
    df = df[new_order]

    # Sort values and write to disk
    df = df.sort_values(["State", "Year"])

    # Add state abbreviations, so I can make a choropleth map with px.choropleth
    df["State Abbrev"] = df["State"].apply(get_abbrev)

    df.to_csv(OUTPUT_FILE, index=False)


if __name__ == "__main__":
    main()


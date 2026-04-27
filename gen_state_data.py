"""Generate the state demographics dataset for the Streamlit workshop.

This script retrieves data from the American Community Survey 1-year Estimates
via the US Census Bureau's API using the censusdis package. The final dataset
structure includes: State, Year, Total Population, Median Household Income,
and State Abbreviation.

Note: Data was not published in 2020 due to COVID-19 pandemic impacts.
See: https://www.census.gov/programs-surveys/acs/data/experimental-data.html
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import us
from censusdis.datasets import ACS1
from censusdis.multiyear import download_multiyear

# Configuration
OUTPUT_FILE = Path("state_data.csv")
START_YEAR = 2005
END_YEAR = 2024
EXCLUDED_YEARS = {2020}  # Data not published due to COVID-19

CENSUS_VARIABLES = {
    "NAME": "State",
    "B01001_001E": "Total Population",
    "B19013_001E": "Median Household Income",
}


def get_state_abbreviation(state_name: str) -> str | None:
    """Get the abbreviation for a state name.

    Args:
        state_name: Full name of the state.

    Returns:
        Two-letter state abbreviation, or None if not found (e.g., Puerto Rico).
    """
    match = us.states.lookup(state_name)
    return match.abbr if match else None


def generate_state_data() -> pd.DataFrame:
    """Generate the state demographics dataset.

    Downloads multi-year census data, processes it, and adds state abbreviations.

    Returns:
        DataFrame with columns: State, Year, Total Population,
        Median Household Income, State Abbrev.
    """
    # Download census data for specified years
    years = [year for year in range(START_YEAR, END_YEAR) if year not in EXCLUDED_YEARS]

    df = download_multiyear(
        dataset=ACS1,
        vintages=years,
        download_variables=list(CENSUS_VARIABLES.keys()),
        state="*",
        rename_vars=False,
        prompt=False,
    )

    # Rename columns to human-readable names
    df = df.rename(columns=CENSUS_VARIABLES)

    # Reorder columns with State and Year first
    cols = df.columns.tolist()
    new_order = ["State", "Year", *[col for col in cols if col not in {"State", "Year"}]]
    df = df[new_order]

    # Sort by state and year
    df = df.sort_values(["State", "Year"])

    # Add state abbreviations for choropleth mapping
    df["State Abbrev"] = df["State"].apply(get_state_abbreviation)

    return df


def main() -> None:
    """Generate and save the state demographics dataset."""
    df = generate_state_data()
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Dataset saved to {OUTPUT_FILE}")
    print(f"Shape: {df.shape}")
    print(f"Years: {sorted(df['Year'].unique())}")


if __name__ == "__main__":
    main()


"""Backend utilities for the Streamlit workshop application.

This module provides data access and visualization functions for US state demographics.
Uses the American Community Survey data to generate interactive plots and data views.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd
import plotly.express as px

if TYPE_CHECKING:
    from plotly.graph_objs import Figure

__all__ = [
    "get_data",
    "get_unique_states",
    "get_unique_years",
    "get_line_graph",
    "get_map",
]

# Constants
DATA_FILE = Path("state_data.csv")


@lru_cache(maxsize=1)
def get_data() -> pd.DataFrame:
    """Load and cache the state demographics dataset.

    Returns:
        DataFrame containing state demographics with columns for State, Year,
        Total Population, Median Household Income, and State Abbrev.

    Raises:
        FileNotFoundError: If the data file does not exist.
        pd.errors.EmptyDataError: If the data file is empty.
    """
    if not DATA_FILE.exists():
        msg = f"Data file not found: {DATA_FILE}"
        raise FileNotFoundError(msg)
    return pd.read_csv(DATA_FILE)


def get_unique_states() -> pd.Index:
    """Get sorted list of unique states from the dataset.

    Returns:
        Index of unique state names sorted alphabetically.
    """
    df = get_data()
    return df["State"].unique()


def get_unique_years() -> pd.Index:
    """Get sorted list of unique years from the dataset.

    Returns:
        Index of unique years in the dataset.
    """
    df = get_data()
    return df["Year"].unique()


def get_line_graph(state: str, demographic: str) -> Figure:
    """Create a line graph showing demographic trends over time for a state.

    Args:
        state: Name of the state to visualize.
        demographic: Column name of the demographic metric to plot.

    Returns:
        Plotly Figure object with the line graph.

    Raises:
        ValueError: If state is not in the dataset.
    """
    df = get_data()

    if state not in df["State"].values:
        msg = f"State '{state}' not found in dataset"
        raise ValueError(msg)

    df_state = df[df["State"] == state]

    return px.line(
        df_state,
        x="Year",
        y=demographic,
        title=f"{demographic} for {state}",
    )


def get_map(demographic: str, year: int) -> Figure:
    """Create a choropleth map showing demographic data across states for a year.

    Args:
        demographic: Column name of the demographic metric to display.
        year: Year to display data for.

    Returns:
        Plotly Figure object with the choropleth map.

    Raises:
        ValueError: If year is not in the dataset.
    """
    df = get_data()

    if year not in df["Year"].values:
        msg = f"Year {year} not found in dataset"
        raise ValueError(msg)

    df_year = df[df["Year"] == year]

    return px.choropleth(
        df_year,
        locations="State Abbrev",
        locationmode="USA-states",
        color=demographic,
        scope="usa",
        color_continuous_scale="Viridis",
        title=f"{demographic} for {year}",
    )


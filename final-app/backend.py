"""Backend data and visualisation helpers for the final Streamlit app."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATA_FILE = Path(__file__).parent / "state_data.csv"

COL_STATE = "State"
COL_YEAR = "Year"
COL_STATE_ABBREV = "State Abbrev"

DEMOGRAPHICS: list[str] = ["Total Population", "Median Household Income"]

# ---------------------------------------------------------------------------
# Data access
# ---------------------------------------------------------------------------


@st.cache_data
def get_data() -> pd.DataFrame:
    """Load the state-level demographics CSV and return it as a DataFrame.

    Results are cached by Streamlit so the file is only read once per session.
    """
    return pd.read_csv(DATA_FILE)


def get_unique_states() -> np.ndarray:
    """Return the unique state names from the dataset."""
    return get_data()[COL_STATE].unique()


def get_unique_years() -> np.ndarray:
    """Return the unique survey years from the dataset."""
    return get_data()[COL_YEAR].unique()


# ---------------------------------------------------------------------------
# Visualisations
# ---------------------------------------------------------------------------


def get_line_graph(state: str, demographic: str) -> go.Figure:
    """Return a Plotly line chart of *demographic* over time for *state*."""
    df = get_data()
    df_state = df[df[COL_STATE] == state]
    return px.line(
        df_state,
        x=COL_YEAR,
        y=demographic,
        title=f"{demographic} for {state}",
    )


def get_map(demographic: str, year: int) -> go.Figure:
    """Return a Plotly choropleth map of *demographic* across all states for *year*."""
    df = get_data()
    df_year = df[df[COL_YEAR] == year]
    return px.choropleth(
        df_year,
        locations=COL_STATE_ABBREV,
        locationmode="USA-states",
        color=demographic,
        scope="usa",
        color_continuous_scale="Viridis",
        title=f"{demographic} for {year}",
    )


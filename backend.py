from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_FILE = "state_data.csv"


@st.cache_data
def get_data() -> pd.DataFrame:
    """Load and cache the state demographics CSV."""
    return pd.read_csv(DATA_FILE)


def get_unique_states() -> list[str]:
    """Return a sorted list of unique state names."""
    return sorted(get_data()["State"].dropna().unique())


def get_unique_years() -> list[int]:
    """Return a sorted list of unique years present in the data."""
    return sorted(get_data()["Year"].unique())


def get_line_graph(state: str, demographic: str) -> px.line:
    """Return a Plotly line chart of *demographic* over time for *state*."""
    df = get_data()
    df_state = df[df["State"] == state]
    return px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")


def get_map(demographic: str, year: int) -> px.choropleth:
    """Return a Plotly choropleth map of *demographic* across all states for *year*."""
    df = get_data()
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


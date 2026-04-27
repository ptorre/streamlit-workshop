"""UI backup – pre-organised version of the 4-ui exercise (reference only)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Demo Streamlit App")

df = pd.read_csv(Path(__file__).parent / "state_data.csv")

DEMOGRAPHICS: list[str] = ["Total Population", "Median Household Income"]

# UI Options
state: str = st.selectbox("Select a State:", df["State"].unique())
demographic: str = st.selectbox("Select a Demographic:", DEMOGRAPHICS)
year: int = st.selectbox("Select a Year:", df["Year"].unique())

# State line graph
df_state = df[df["State"] == state]
fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
st.plotly_chart(fig)

# Map for year
df_year = df[df["Year"] == year]
fig = px.choropleth(
    df_year,
    locations="State Abbrev",
    locationmode="USA-states",
    color=demographic,
    scope="usa",
    title=f"{demographic} for {year}",
    color_continuous_scale="Viridis",
)
st.plotly_chart(fig)

# All data for completeness
st.dataframe(df)


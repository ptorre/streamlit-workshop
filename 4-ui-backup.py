"""Organizing the User Interface - Multiple widgets and visualizations (backup).

This module demonstrates how to create a more complex Streamlit app with
multiple input widgets, line graphs, and choropleth maps.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Constants
DATA_FILE = Path("state_data.csv")
DEMOGRAPHICS = ["Total Population", "Median Household Income"]

st.title("Demo Streamlit App")

df = pd.read_csv(DATA_FILE)

# UI Options
state = st.selectbox("Select a State:", df["State"].unique())
demographic = st.selectbox("Select a Demographic:", DEMOGRAPHICS)
year = st.selectbox("Select a Year:", df["Year"].unique())

# State line graph
df_state = df[df["State"] == state]
fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
st.plotly_chart(fig)

# Map for year
df_year = df[df["Year"] == year]

fig = px.choropleth(
    df_year,
    locations="State Abbrev",  # Column for region
    locationmode="USA-states",
    color=demographic,  # Column for color
    scope="usa",
    title=f"{demographic} for {year}",
    color_continuous_scale="viridis",
)
st.plotly_chart(fig)

# All data for completeness
st.dataframe(df)

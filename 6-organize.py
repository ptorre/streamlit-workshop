"""Advanced UI Organization - Columns and tabs.

This module demonstrates advanced Streamlit UI organization techniques including
column layouts and tabbed interfaces for a polished user experience.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Constants
DATA_FILE = Path("state_data.csv")
DEMOGRAPHICS = ["Total Population", "Median Household Income"]
TAB_LABELS = ["📈 Graph", "🗺️ Map", "📊 Table"]

st.title("Demo Streamlit App")

df = pd.read_csv(DATA_FILE)

col1, col2, col3 = st.columns(3)
with col1:
    state = st.selectbox("State:", df["State"].unique())
with col2:
    demographic = st.selectbox("Demographic:", DEMOGRAPHICS)
with col3:
    year = st.selectbox("Year:", df["Year"].unique())

graph_tab, map_tab, table_tab = st.tabs(TAB_LABELS)
with graph_tab:
    # State line graph
    df_state = df[df["State"] == state]
    fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
    st.plotly_chart(fig)
with map_tab:
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
with table_tab:
    # All data for completeness
    st.dataframe(df)

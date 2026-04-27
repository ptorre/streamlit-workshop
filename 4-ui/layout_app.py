from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).parent.parent / "state_data.csv"

DEMOGRAPHICS = ["Total Population", "Median Household Income"]


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


st.title("Demo Streamlit App")

df = load_data()

# UI Options
state = st.selectbox("Select a State:", sorted(df["State"].dropna().unique()))
demographic = st.selectbox("Select a Demographic:", DEMOGRAPHICS)
year = st.selectbox("Select a Year:", sorted(df["Year"].unique()))

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
    color_continuous_scale="viridis",
)
st.plotly_chart(fig)

# All data for completeness
st.dataframe(df)


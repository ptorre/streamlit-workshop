from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

DEMOGRAPHICS = ["Total Population", "Median Household Income"]


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv("state_data.csv")


st.title("Demo Streamlit App")

df = load_data()

col1, col2, col3 = st.columns(3)
with col1:
    state = st.selectbox("State:", sorted(df["State"].dropna().unique()))
with col2:
    demographic = st.selectbox("Demographic:", DEMOGRAPHICS)
with col3:
    year = st.selectbox("Year:", sorted(df["Year"].unique()))

graph_tab, map_tab, table_tab = st.tabs(["📈 Graph", "🗺️ Map", "📊 Table"])
with graph_tab:
    df_state = df[df["State"] == state]
    fig = px.line(df_state, x="Year", y=demographic, title=f"{demographic} for {state}")
    st.plotly_chart(fig)
with map_tab:
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
with table_tab:
    st.dataframe(df)


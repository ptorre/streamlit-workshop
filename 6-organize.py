"""Organize exercise – split UI from logic using a backend module."""

from __future__ import annotations

import streamlit as st

import backend as be

st.title("Demo Streamlit App")

col1, col2, col3 = st.columns(3)
with col1:
    state: str = st.selectbox("State:", be.get_unique_states())
with col2:
    demographic: str = st.selectbox("Demographic:", be.DEMOGRAPHICS)
with col3:
    year: int = st.selectbox("Year:", be.get_unique_years())

graph_tab, map_tab, table_tab = st.tabs(["📈 Graph", "🗺️ Map", "📊 Table"])
with graph_tab:
    st.plotly_chart(be.get_line_graph(state, demographic))
with map_tab:
    st.plotly_chart(be.get_map(demographic, year))
with table_tab:
    st.dataframe(be.get_data())


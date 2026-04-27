"""US State Demographics Dashboard.

A Streamlit application for visualizing US state demographic data from the
American Community Survey. Users can explore population and income trends
through interactive graphs, maps, and data tables.
"""

from __future__ import annotations

import streamlit as st

import backend as be

# Constants
DEMOGRAPHICS = ["Total Population", "Median Household Income"]
TAB_ICONS = ["📈", "🗺️", "📊"]
TAB_NAMES = ["Graph", "Map", "Table"]


def main() -> None:
    """Run the Streamlit dashboard application."""
    st.title("US State Demographics")

    # User input controls in three columns
    col1, col2, col3 = st.columns(3)
    with col1:
        state = st.selectbox("State:", be.get_unique_states())
    with col2:
        demographic = st.selectbox("Demographic:", DEMOGRAPHICS)
    with col3:
        year = st.selectbox("Year:", be.get_unique_years())

    # Create tabs for different visualizations
    tab_labels = [f"{icon} {name}" for icon, name in zip(TAB_ICONS, TAB_NAMES, strict=True)]
    graph_tab, map_tab, table_tab = st.tabs(tab_labels)

    with graph_tab:
        fig = be.get_line_graph(state, demographic)
        st.plotly_chart(fig)

    with map_tab:
        fig = be.get_map(demographic, year)
        st.plotly_chart(fig)

    with table_tab:
        df = be.get_data()
        st.dataframe(df)


if __name__ == "__main__":
    main()


from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_PATH = Path(__file__).parent.parent / "state_data.csv"

DEMOGRAPHICS: dict[str, str] = {
    "Population": "Total Population",
    "Median Household Income": "Median Household Income",
}


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


st.title("Demo Streamlit App")

df = load_data()

states = sorted(df["State"].dropna().unique())
selected_states = st.multiselect("Select one or more states:", states, default=None)

metric_label = st.selectbox("Choose y-axis value:", list(DEMOGRAPHICS.keys()))
y_column = DEMOGRAPHICS[metric_label]
use_log_scale = st.toggle("Use log scale", value=False)
show_indexed = st.toggle("Show indexed growth (first year = 100)", value=False)
show_small_multiples = st.toggle("Show small multiples", value=False)

if not selected_states:
    st.info("Select at least one state to see the chart.")
else:
    df_selected = df[df["State"].isin(selected_states)].sort_values(["State", "Year"])
    plot_df = df_selected.copy()
    plot_y = y_column
    title_metric = metric_label

    if show_indexed:
        first_values = plot_df.groupby("State")[y_column].transform("first")
        plot_df["Indexed Value"] = (plot_df[y_column] / first_values) * 100
        plot_y = "Indexed Value"
        title_metric = f"{metric_label} Indexed (First Year = 100)"

    title = f"{title_metric} Over Time by State"
    if use_log_scale:
        title = f"{title} (Log Scale)"

    if show_small_multiples:
        fig = px.line(
            plot_df,
            x="Year",
            y=plot_y,
            color="State",
            facet_col="State",
            facet_col_wrap=3,
            markers=True,
            title=title,
        )
    else:
        fig = px.line(
            plot_df,
            x="Year",
            y=plot_y,
            color="State",
            markers=True,
            title=title,
        )

    if use_log_scale:
        fig.update_yaxes(type="log")

    fig.update_layout(legend_title_text="State")

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_selected)

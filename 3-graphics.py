"""Graphics exercise – add a line chart filtered by the selected state."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

st.title("Demo Streamlit App")

df = pd.read_csv(Path(__file__).parent / "state_data.csv")

state: str = st.selectbox("Select a State:", df["State"].unique())

df_state = df[df["State"] == state]

st.dataframe(df_state)

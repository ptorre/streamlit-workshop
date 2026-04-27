"""Creating Interactive Graphics - Plotly visualizations.

This module demonstrates how to filter data and create visualizations
using Plotly Express with Streamlit.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Constants
DATA_FILE = Path("state_data.csv")

st.title("Demo Streamlit App")

df = pd.read_csv(DATA_FILE)

state = st.selectbox("Select a State:", df["State"].unique())

df_state = df[df["State"] == state]

st.dataframe(df_state)

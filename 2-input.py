"""Input exercise – let the user filter the dataset by state."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

st.title("Demo Streamlit App")

df = pd.read_csv(Path(__file__).parent / "state_data.csv")

# Exercise: Change this code to:
# 1. Ask the user to select a state
# 2. Have it populate with all the list of unique states
option: str = st.selectbox("Select your favorite fruit:", ["Apple", "Banana", "Cherry"])

st.write("You selected:", option)

# Filter df to just the values the user selected
# df = ...

st.dataframe(df)

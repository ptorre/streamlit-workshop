"""Working with User Input - Interactive state selection.

This module demonstrates how to create user input widgets in Streamlit
and filter data based on user selections.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

# Constants
DATA_FILE = Path("state_data.csv")

st.title("Demo Streamlit App")

df = pd.read_csv(DATA_FILE)

# Exercise: Change this code to:
# 1. Ask the user to select a state
# 2. Have it populate with all the list of unique states
option = st.selectbox("Select your favorite fruit:", ["Apple", "Banana", "Cherry"])

st.write("You selected:", option)

# Filter df to just the values the user selected
# df = ...

st.dataframe(df)

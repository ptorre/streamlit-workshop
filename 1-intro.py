"""Introduction to Streamlit - Basic data display.

This module demonstrates the simplest Streamlit app that loads and displays data.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

# Constants
DATA_FILE = Path("state_data.csv")

# st.title("Demo Streamlit App")

df = pd.read_csv(DATA_FILE)

st.dataframe(df)


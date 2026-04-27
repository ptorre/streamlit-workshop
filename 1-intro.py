"""Intro exercise – display the raw state-level demographics dataset."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st

# st.title("Demo Streamlit App")

df = pd.read_csv(Path(__file__).parent / "state_data.csv")

st.dataframe(df)

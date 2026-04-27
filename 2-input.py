from __future__ import annotations

import pandas as pd
import streamlit as st


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv("state_data.csv")


st.title("Demo Streamlit App")

df = load_data()

# Exercise: Change this code to:
# 1. Ask the user to select a state
# 2. Have it populate with all the list of unique states
option = st.selectbox("Select your favorite fruit:", ["Apple", "Banana", "Cherry"])

st.write("You selected:", option)

# Filter df to just the values the user selected
# df = ...

st.dataframe(df)

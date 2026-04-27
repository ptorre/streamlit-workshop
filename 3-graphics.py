from __future__ import annotations

import pandas as pd
import streamlit as st


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv("state_data.csv")


st.title("Demo Streamlit App")

df = load_data()

state = st.selectbox("Select a State:", sorted(df["State"].dropna().unique()))

df_state = df[df["State"] == state]

st.dataframe(df_state)

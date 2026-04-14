import streamlit as st
import pandas as pd

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

# Exercise: Change this code to:
# 1. Ask the user to select a state
# 2. Have it populate with all the list of unique states
states = sorted(df["State"].dropna().unique())
option = st.selectbox("Select a state:", states)

st.write("You selected:", option)

# Filter df to just the values the user selected
df = df[df["State"] == option]

st.dataframe(df)

st.divider()
st.subheader("Other common input widgets")

name = st.text_input("Your name", placeholder="Type your name")
age = st.slider("Age", min_value=0, max_value=100, value=30)
show_raw_data = st.checkbox("Show raw data", value=False)
favorite_states = st.multiselect(
	"Pick one or more favorite states",
	states,
	default=states[:3],
)

st.write("Widget demo output")
st.write("Name:", name if name else "(not provided)")
st.write("Age:", age)
st.write("Show raw data:", show_raw_data)
st.write("Favorite states:", favorite_states if favorite_states else "(none selected)")

if show_raw_data:
	st.dataframe(pd.read_csv("state_data.csv"))

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Streamlit App")

df = pd.read_csv("state_data.csv")

state = st.selectbox("Select a State:", df["State"].unique())
demographic = st.selectbox(
    "Select a Demographic:", ["Total Population", ["Median Household Income"]]
)
year = st.selectbox("Year:", df["Year"].unique())

mask = df["State"] == state
df_state = df[mask]
fig = px.line(
    df_state, x="Year", y="Total Population", title="Population of California over Time"
)
st.plotly_chart(fig)


mask = df["Year"] == year
df_choro = df[mask]

fig = px.choropleth(
    df_choro,
    locations="State Abbrev",  # Column for region
    locationmode="USA-states",
    color="Total Population",  # Column for color
    scope="usa",
    title=f"{year} {demographic}",
    color_continuous_scale="viridis",
)
st.plotly_chart(fig)

st.dataframe(df_state)

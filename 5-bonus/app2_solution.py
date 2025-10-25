import streamlit as st
import backend as be
import plotly.express as px

st.title("Comparing Percent Change in Demographics")

years = be.get_unique_years_as_strings()
col1, col2, col3 = st.columns(3)
with col1:
    year1 = st.selectbox("Year 1: ", years)
with col2:
    year2 = st.selectbox("year 2: ", years[1:])
with col3:
    demographic = st.selectbox(
        "Demographic: ", ["Total Population", "Median Household Income"]
    )

df_wide = be.get_data_wide(demographic)

cols = ["State", "State Abbrev", year1, year2]
df_wide = df_wide[cols]

df_wide["Diff"] = (df_wide[year2] - df_wide[year1]) / df_wide[year1] * 100
df_wide.head()

map_tab, table_tab = st.tabs(["Map", "Table"])
with map_tab:
    fig = px.choropleth(
        df_wide,
        locations="State Abbrev",  # Column for region
        locationmode="USA-states",
        color="Diff",  # Column for color
        scope="usa",
        color_continuous_scale="Viridis",
        title=f"Percent Change in {demographic}: {year1}-{year2}",
    )
    st.plotly_chart(fig)
with table_tab:
    st.dataframe(df_wide)

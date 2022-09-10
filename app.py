import pandas as pd
import streamlit as st

import helper
import preprocessor

df = pd.read_csv("./dataset/athlete_events.csv")
region_df = pd.read_csv("./dataset/noc_regions.csv")

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("120 Years Of Olympics Data")

user_menu = st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall analysis", "Country wise analysis", "Athlete wise analysis")
)

if user_menu == "Medal Tally":
    st.sidebar.header("Medal Tally")
    years, countries = helper.country_years_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", countries)
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    elif selected_year == "Overall" and selected_country != "Overall":
        st.title(selected_country + " Overall performance")
    elif selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    elif selected_year != "Overall" and selected_country != "Overall":
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

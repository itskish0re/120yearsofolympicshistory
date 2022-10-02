import pandas as pd
import streamlit as st

import helper
import preprocessor
import plotly.express as px

df = pd.read_csv("./dataset/athlete_events.csv")
region_df = pd.read_csv("./dataset/noc_regions.csv")

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("120 Years Of Olympics Data")

user_menu = st.sidebar.radio(
    "Select an option",
    ("Medal Tally", "Overall Analysis", "Country Wise Analysis", "Athlete Wise Analysis")
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

if user_menu == "Overall Analysis":
    edition = df["Year"].unique().shape[0]-1
    cities = df["City"].unique().shape[0]
    sports = df["Sport"].unique().shape[0]
    events = df["Event"].unique().shape[0]
    athletes = df["Name"].unique().shape[0]
    nations = df["region"].unique().shape[0]

    st.title("Top Statstics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(edition)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Nations")
        st.title(nations)

    st.title("Participationg nations over years")
    nations_over_time = helper.participation_nations_over_time(df)
    fig = px.line(nations_over_time, x="Edition", y="No. of Countries")
    st.plotly_chart(fig)

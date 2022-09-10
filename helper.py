import numpy as np


def fetch_medal_tally(df, year, country):
    medal_tally = df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
    medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]
    if year == "Overall" and country == "Overall":
        medal_tally = medal_tally.groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold", ascending=False).reset_index()
    elif year == "Overall" and country != "Overall":
        medal_tally = medal_tally[medal_tally["region"] == country].groupby("Year").sum()[
            ["Gold", "Silver", "Bronze"]].sort_values("Year").reset_index()
    elif year != "Overall" and country == "Overall":
        medal_tally = medal_tally[medal_tally["Year"] == int(year)].groupby("region").sum()[
            ["Gold", "Silver", "Bronze"]].sort_values("Gold", ascending=False).reset_index()
    elif year != "Overall" and country != "Overall":
        medal_tally = medal_tally[(medal_tally["Year"] == int(year)) & (medal_tally["region"] == country)]
        medal_tally = medal_tally.groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold", ascending=False).reset_index()
    return medal_tally


def country_years_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0, "Overall")
    countries = np.unique(df["region"].dropna().values).tolist()
    countries.sort()
    countries.insert(0, "Overall")
    return years, countries

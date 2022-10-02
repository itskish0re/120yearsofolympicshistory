import numpy as np


def fetch_medal_tally(df, year, country):
    medal_tally = df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
    medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]
    if year == "Overall" and country == "Overall":
        medal_tally = medal_tally.groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold",
                                                                                                    ascending=False).reset_index()
    elif year == "Overall" and country != "Overall":
        medal_tally = medal_tally[medal_tally["region"] == country].groupby("Year").sum()[
            ["Gold", "Silver", "Bronze"]].sort_values("Year").reset_index()
    elif year != "Overall" and country == "Overall":
        medal_tally = medal_tally[medal_tally["Year"] == int(year)].groupby("region").sum()[
            ["Gold", "Silver", "Bronze"]].sort_values("Gold", ascending=False).reset_index()
    elif year != "Overall" and country != "Overall":
        medal_tally = medal_tally[(medal_tally["Year"] == int(year)) & (medal_tally["region"] == country)]
        medal_tally = medal_tally.groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold",
                                                                                                    ascending=False).reset_index()
    return medal_tally


def country_years_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0, "Overall")
    countries = np.unique(df["region"].dropna().values).tolist()
    countries.sort()
    countries.insert(0, "Overall")
    return years, countries


def data_over_time(df, col):
    d_over_time = df.drop_duplicates(["Year", col])["Year"].value_counts().reset_index().sort_values("index")
    d_over_time.rename(columns={"index": "Edition", "Year": col}, inplace=True)
    return d_over_time


def most_successful(df, sport):
    temp_df = df.dropna(subset=["Medal"])
    if sport != "Overall":
        temp_df = temp_df[temp_df["Sport"] == sport]
    x = temp_df["Name"].value_counts().reset_index().head(15).merge(df, left_on="index", right_on="Name", how="left")[["index", "Name_x", "Sport", "region"]].drop_duplicates("index")
    x.rename(columns={"index": "Name", "Name_x": "Medals"}, inplace=True)
    return x


def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"], inplace=True)
    return temp_df[temp_df["region"] == country].groupby("Year").count()["Medal"].reset_index()


def countrywise_event_heatmap(df, country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"], inplace=True)
    pt = temp_df[temp_df["region"] == country].pivot_table(index="Sport", columns="Year", values="Medal", aggfunc="count").fillna(0)
    return pt


def most_successful_countrywise(df, country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df = temp_df[temp_df["region"] == country]
    x = temp_df["Name"].value_counts().reset_index().head(10).merge(df, left_on="index", right_on="Name", how="left")[
        ["index", "Name_x", "Sport"]].drop_duplicates("index")
    x.rename(columns={"index": "Name", "Name_x": "Medals"}, inplace=True)
    return x

def medal_tally(mtdf):
    tally = mtdf.drop_duplicates(subset=["Team", "Noc", "Games", "Year", "City", "Sport", "Event", "Medal"]).groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold", ascending=False).reset_index()
    tally["Total"] = tally["Gold"] + tally["Silver"] + tally["Bronze"]
    tally["Gold"] = tally["Gold"].astype("int")
    tally["Silver"] = tally["Silver"].astype("int")
    tally["Bronze"] = tally["Bronze"].astype("int")
    return tally


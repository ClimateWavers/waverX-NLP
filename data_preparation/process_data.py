import pandas as pd
"""
Anaylse data, filter categories and append right data to dataset
"""

tweet = pd.read_csv("dataset/tweets.csv")

labels = ["Earthquake", "Drought",
          "Damaged Infrastructure", "Human Damage", "Human", "Land Slide", "Non Damage Buildings and  Street", "Non Damage Wildlife Forest",
          "Sea", "Urban Fire", "Wild Fire", "Water Disaster"]


for index, row in tweet.iterrows():
    keyword = row["keyword"]
    print(keyword)
    keyword = keyword.capitalize()
    if keyword == "Aftershock":
        keyword = "Earthquake"
    elif keyword == "Bridge collapse":
        keyword = "Damaged Infrastructure"
    elif keyword == "Buildings burning" or keyword == "Buildings on fire":
        keyword = "Urban Fire"
    elif keyword == "Burning" or keyword == "Burned" or keyword == "Bush fires":
        keyword = "Wild Fire"
    elif keyword == "Catastrophic":
        if "fire" in row["text"]:
            keyword = "Wild Fire"
        elif "earthquake" in row["text"]:
            keyword = "Earthquake"
    elif "flood" in keyword:
        keyword = "Water Disaster"
    elif "wild" in keyword:
        keyword = "Wild Fire"
    print(f"New {keyword}")
    if keyword in labels:
        text = str(row["text"])
        label = keyword
        dataset = pd.DataFrame([[text, label]])
        dataset.to_csv("dataset/" + "disaster_text.csv",
                   mode='a', header=False, index=False)

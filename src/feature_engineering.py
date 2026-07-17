import pandas as pd


def create_features(df):
    """
    Creates engineered features for the Titanic dataset.
    """

    df = df.copy()

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

    df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")

    df["Title"] = df["Title"].replace({"Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs"})

    df["Title"] = df["Title"].replace(
        [
            "Lady",
            "Countess",
            "Capt",
            "Col",
            "Don",
            "Dr",
            "Major",
            "Rev",
            "Sir",
            "Jonkheer",
            "Dona",
        ],
        "Rare",
    )

    df["CabinKnown"] = df["Cabin"].notna().astype(int)

    df["Deck"] = df["Cabin"].fillna("U").str[0]

    df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

    df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100], labels=False)

    return df

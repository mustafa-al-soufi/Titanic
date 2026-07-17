import numpy as np
import pandas as pd


def print_title(title):
    """Print a formatted section title."""

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def dataframe_summary(df):
    """Print basic dataframe information."""

    print(df.info())
    print()
    print(df.describe(include="all"))


def missing_values(df):
    """Return missing values sorted descending."""

    return df.isnull().sum().sort_values(ascending=False)


def save_dataframe(df, filename):
    """Save dataframe as csv."""

    df.to_csv(filename, index=False)


def load_dataframe(path):
    """Load csv file."""

    return pd.read_csv(path)

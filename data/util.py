import pandas as pd
import os


def get_data(PATH):
    df = pd.read_csv(PATH)
    df["Price_in_thousands"].fillna(method="bfill",inplace=True)
    return df


"""
Main cli or app entry point
"""

import polars as pl
import matplotlib.pyplot as plt

# define a function to provide descriptive statistics of a dataset


def desripStats(file):
    # use panda to read csv file
    df = pl.read_csv(file)

    # quick glimpse of the data
    print(df.head())
    # print(df.describe())

    # check data information
    # print(df.info())

    # check unique values for each colunm
    # print(df.nunique())

    # plot a scatter graph
    plt.scatter(df["wt"], df["mpg"])
    plt.xlabel("Weight, lbs")
    plt.ylabel("Miles per Gallon, miles")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()

    return df.describe()

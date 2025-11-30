# engine.py

import pandas as pd
import numpy as np
import sys
import os
import time
import matplotlib.pyplot as plt

from summary import sales_summary
from cli_utils import clear_screen, anim
from utils import proceed, convert


# Output folders (auto-created even if empty)
CL_DIR = "cleaned_data"
PLOTS_DIR = "images"
os.makedirs(CL_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

# Pandas display settings for cleaner terminal output
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', None)

END = "\n[Program finished.]"
ERROR = "Oops! Something went wrong.\n"


def load_data():
    """
    Ask the user to provide a CSV file path and load it into a DataFrame.

    Keeps asking until the path is valid.
    Returns a copy of the DataFrame so the original file isn't affected.
    """
    loading = True
    while loading:
        csv_file = input("\nUpload your CSV filepath: ").strip()

        if not csv_file:
            print("Input field cannot be empty!")
            continue

        try:
            df = pd.read_csv(csv_file)
            loading = False
            return df.copy()
        except Exception as e:
            print(f"{ERROR}{e}")


def inspect_data(df, display=False):
    """
    Print dataset previews and stats if display=True.

    Used mainly for debugging or inspecting data before cleaning.
    """
    if display:
        print("Dataset Preview:")
        print(df.head(), "\n")

        print("Dataset Shape (rows, columns):")
        print(df.shape, "\n")

        print("Column Data Types:")
        print(df.dtypes, "\n")

        print("Summary Statistics:")
        print(df.describe(), "\n")


def clean_data(df):
    """
    Clean raw sales data and return a cleaned DataFrame + rows with missing values.

    Steps:
    - Fix column naming (Title Case)
    - Convert Price, Quantity → numeric
    - Convert Sale_Date → datetime
    - Remove invalid rows (Price ≤ 0 or Quantity ≤ 0)
    - Fill missing Category/Region with 'Unknown'
    - Add Revenue column
    """
    inspect_data(df, display=False)

    # Normalize column names for consistent processing
    df.columns = df.columns.str.title()

    # Type conversions (using your convert() helper)
    df["Price"] = convert(df, "Price", cvrt="num")
    df["Quantity"] = convert(df, "Quantity", cvrt="num")
    df["Sale_Date"] = convert(df, "Sale_Date", cvrt="dt")

    # Remove rows with non-sensical values
    invalid_rows = df[(df.Price <= 0) | (df.Quantity <= 0)]
    df = df.drop(invalid_rows.index)

    # Save rows that originally had missing keys (Category/Region)
    missing = df[(df.Category.isna()) | (df.Region.isna())]

    # Fill missing text fields with "Unknown"
    df[["Category", "Region"]] = df[["Category", "Region"]].fillna("Unknown")

    # Compute revenue
    df["Revenue"] = df.Price * df.Quantity

    return df, missing


def calculate_sales(df, col1="Category", col2="Revenue"):
    """
    Group by category (or any column) and sum revenue.

    Returns a sorted Series from highest → lowest revenue.
    """
    return df.groupby(col1)[col2].sum().sort_values(ascending=False)


def tier_split(df, col1="Category", col2="Revenue"):
    """
    Split category sales into three roughly equal tiers:
    - Top
    - Middle
    - Bottom

    df should be a Series or grouped object.
    Returns three DataFrames (top, middle, bottom).
    """
    cat_sales_df = df.reset_index()
    cat_sales_df.columns = [col1, col2]

    n = len(cat_sales_df)
    k = 3  # number of tiers
    chunk = n // k  # size of each tier

    return (
        cat_sales_df.iloc[:chunk],
        cat_sales_df.iloc[chunk : chunk * 2],
        cat_sales_df.iloc[chunk * 2 :],
    )


def create_plot(df, k="bar", rt=0, fp="cat_sales.png", can_plot=False):
    """
    Generate and save a plot of category sales.

    Only runs if can_plot=True.

    Parameters:
    - k : chart type ('bar', 'line', etc.)
    - rt: rotation angle for x-axis labels
    - fp: filename for the output image
    """
    if can_plot:
        plt.figure(figsize=(12, 6))

        df.plot(kind=k)
        plt.xticks(rotation=rt)

        plt.savefig(os.path.join(PLOTS_DIR, fp), dpi=300)
        plt.close()

        print(f'\n"{fp}" saved successfully.')
        time.sleep(2)


def save_cleaned_data(df, fmt="csv", fp="sales_cleaned", can_save=False):
    """
    Save the cleaned dataset into /cleaned_data.

    Supports CSV (default) and Excel output.
    Only runs if can_save=True.
    """
    if can_save:
        if fmt.lower() == "csv":
            df.to_csv(os.path.join(CL_DIR, f"{fp}.csv"), index=False)
        elif fmt.lower() == "excel":
            df.to_excel(os.path.join(CL_DIR, f"{fp}.xlsx"), index=False)
        else:
            # fallback to CSV if user gives unsupported format
            df.to_csv(os.path.join(CL_DIR, f"{fp}.csv"), index=False)

        print(f'\n"{fp}" saved successfully.')
# utils.py
import pandas as pd

# Simple yes/no options for user prompts
YES = ["yes", "y"]
NO = ["no", "n"]


def proceed(text):
    """
    Ask the user a yes/no question and return True or False.

    Keeps asking until the user enters a valid response.
    Example:
        proceed("Continue")  → True/False
    """
    requesting = True

    while requesting:
        req = input(f"{text}? (y/n): ").lower().strip()

        if req in YES:
            requesting = False
            return True

        elif req in NO:
            requesting = False
            return False

        else:
            # When the user types something unexpected
            print("Invalid input! Please type 'y' or 'n'.")


def convert(df, col, cvrt="num"):
    """
    Convert a DataFrame column into a specific data type.

    Parameters:
        df   : DataFrame containing the column
        col  : name of the column to convert
        cvrt : 'num' for numeric, 'dt' for datetime

    Returns:
        Converted Series.
    """
    data = df  # just referencing the same df for clarity

    if cvrt.lower() == "num":
        # Convert to integer/float
        return pd.to_numeric(data[col], errors="coerce")

    elif cvrt.lower() == "dt":
        # Convert to datetime; invalid dates become NaT instead of errors
        return pd.to_datetime(data[col], errors="coerce")

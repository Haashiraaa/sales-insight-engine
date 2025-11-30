# summary.py

import textwrap

# Decorative header for the report
LINES = "=" * 11

# General analysis text shown below every summary
ANALYSIS = (
    "The top-performing categories make up the biggest share of revenue, "
    "showing strong customer demand and reliable sales strength. The mid-range "
    "categories perform steadily and could benefit from targeted promotions or "
    "slightly increased visibility. Lower-ranked categories move slower and may "
    "need pricing adjustments, better placement, or more marketing push. "
    "Overall, the spread shows clear leaders, stable performers, and areas that "
    "may require review."
)


def format_text(text, width=70):
    """
    Wrap long text to fit nicely on smaller screens (e.g., phones).

    Parameters:
        text (str): The text you want wrapped.
        width (int): Max characters per line.

    Returns:
        str: The wrapped text.
    """
    wrapper = textwrap.TextWrapper(width=width)
    formatted = []

    for line in text.split("\n"):
        if not line.strip():
            formatted.append("")  # keep blank lines
        else:
            formatted.append(wrapper.fill(line))

    return "\n".join(formatted)


def sales_summary(nr, mv, top, middle, bottom, col1="Category", col2="Revenue"):
    """
    Print a clean, structured sales summary to the terminal.

    Parameters:
        nr (DataFrame): The cleaned dataframe (used for total row count).
        mv (DataFrame): Rows with missing values before cleaning.
        top (DataFrame): Top tier categories.
        middle (DataFrame): Middle tier categories.
        bottom (DataFrame): Bottom tier categories.
        col1 (str): Column name for categories.
        col2 (str): Column name for revenue.

    This function only displays results — it doesn’t save anything.
    """
    print(f"{LINES} Sales Summary {LINES}")

    # Basic overview
    print(f"\nTotal Rows: {len(nr)}")
    print(f"Missing Values Handled: {len(mv)}")

    # Top categories
    print("\nTop Category:")
    for _, row in top.iterrows():
        print(f"{row[col1]} - ${row[col2]:,.2f}")

    # Middle categories
    print("\nMiddle Categories:")
    for _, row in middle.iterrows():
        print(f"{row[col1]} - ${row[col2]:,.2f}")

    # Lowest categories
    print("\nLowest Category:")
    for _, row in bottom.iterrows():
        print(f"{row[col1]} - ${row[col2]:,.2f}")

    # Insight section
    print("\nOverall Insights:")
    print(format_text(ANALYSIS))

    print("\n-------------------------------------")

    # If Unknown exists, display a gentle note (no assumptions)
    if "Unknown" in nr[col1].values:
        print("\nNote: Some entries fall under 'Unknown'.")
        print("This may simply represent missing labels or newly introduced items.")
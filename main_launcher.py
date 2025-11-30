# main_launcher.py

import sys

from engine import (
    load_data,
    clean_data,
    calculate_sales,
    create_plot,
    tier_split,
    save_cleaned_data,
    END,
    ERROR,
)
from utils import proceed
from cli_utils import clear_screen, anim
from summary import sales_summary


def main():
    """
    Main entry point for running the full sales processing pipeline.

    Workflow:
    1. Load raw sales data.
    2. Clean the data (handle missing values, fix types).
    3. Calculate total revenue per category.
    4. Optionally generate plots.
    5. Split categories into top/middle/bottom tiers.
    6. Ask user if they want a summary.
    7. Save cleaned data to the output folder.

    This function basically ties all modules together and runs the full engine.
    """
    
    # Load the raw sales CSV file
    sales = load_data()

    # Clear the terminal so the next output looks clean
    clear_screen()

    # Clean dataset → returns cleaned dataframe + number of missing values handled
    cleaned_data, missing_data = clean_data(sales)

    # Calculate revenue per category
    cat_sales = calculate_sales(cleaned_data)

    # Create visualization (plot disabled by default unless user requests)
    create_plot(cat_sales, can_plot=False)

    # Break categories into top/middle/bottom tiers
    top_reg, middle_reg, bottom_reg = tier_split(cat_sales)

    # Ask user if they want to see the text-based sales summary
    req_to_sum = proceed("\nProceed to view sales summary")

    if req_to_sum:
        # Tiny animation while "generating" the summary
        anim(text="\rGenerating summary")

        # Display sales summary in a clean organized format
        sales_summary(cleaned_data, missing_data, top_reg, middle_reg, bottom_reg)

    # Save cleaned dataset (disabled unless user chooses it)
    save_cleaned_data(cleaned_data, can_save=False)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Show error in a friendly formatted message
        print(f"\n{ERROR}{e}")
    except KeyboardInterrupt:
        # Gracefully exit if user presses CTRL+C
        print("\n", END)
        sys.exit()
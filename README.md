
## Sales Insight Engine

A lightweight and modular **Python CLI tool** for cleaning sales datasets, calculating category-level revenue, generating insights, and producing structured summaries.  
Designed to run smoothly in any environment — even on a phone — using only standard Python libraries and pandas.

---

## Features

- **CSV import + automatic validation**
- **Cleaning pipeline**
  - fixes column names
  - converts numeric + date fields
  - removes invalid rows
  - fills missing labels with `"Unknown"`
- **Revenue calculation**
- **Top / Middle / Bottom category grouping**
- **Optional plot generation**
- **Optional saving of cleaned CSV/Excel**
- **Neat, mobile-friendly summary output**
- **Completely modular codebase**

---

## Project Structure

sales-insight-engine/ │ ├── main_launcher.py       # Entry point for running the tool <br>├── engine.py              # Loading, cleaning, revenue logic, plots <br>├── utils.py               # Helpers: convert(), proceed() <br>├── cli_utils.py           # Terminal clearing + loading animation <br>├── summary.py             # Formatted sales summary │ <br>├── cleaned_data/          # Auto-created output folder <br>└── images/                # Auto-created plot folder

---

## How to Run

```bash
git clone https://github.com/Haashiraaa/sales-insight-engine.git
cd sales-insight-engine

python main_launcher.py
```
You will be asked to upload your CSV file path:

Upload your CSV filepath:

The tool will handle the rest:

cleaning

revenue calculation

performance tiers

optional saving

formatted summary



---

## Optional Plotting

Inside engine.py, you can enable plot generation by setting:

create_plot(cat_sales, can_plot=True)

Plots are saved to the images/ folder.


---

## Saving the Cleaned Dataset

Enable saving by toggling:

save_cleaned_data(cleaned_data, can_save=True)

Supports:

CSV
Excel



---

## Clean Output Example
```bash
=========== Sales Summary ===========
Total Rows: 4500
Missing Values Handled: 12

Top Category:
Electronics - $1,204,500.00
...

Overall Insights:
The top-performing categories are driving the largest share...
```

---

## Requirements

Python 3.10+

pandas

matplotlib


Install with:
```bash
pip install pandas matplotlib
```

---

## Design Philosophy

Simple, readable modules

Phone-friendly CLI output

No in-place mutation

Optional heavy operations (plots, saving)

Safe defaults — always off until enabled



---

## License

MIT License — free to use and modify.


---

## Contributing

Feel free to open issues or submit pull requests if you’d like to extend the tool (extra plots, more metrics, dashboards, etc.).

---

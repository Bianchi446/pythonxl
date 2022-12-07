from pathlib import Path
import pandas as pd


# Script : Read all Excel files, aggregate data and write summary table into new Excel


# <1> Directorory of this file

this_dir = Path(__file__).resolve().parent


# <2> Read all excel files from all subfolders of sales_data
parts = []
 
for path in (this_dir / "sales_data").rglob("*.xls*"):
    print(f"Reading {path.name}")
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)

# <3> Combine data frames of each file into a single data frame

df = pd.concat(parts)

# <4> Pivot each store into a column and sum up all transactions per date

pivot = pd.pivot_table(df, index="transaction_date", columns="store", values="amount", aggfunc="sum")


# <5> Resample to end of month and assign an index name 

summary = pivot.resample("M").sum()
summary.index.name = "Month"

# <6> Write summary report to excel file 

summary.to_excel(this_dir / "sales_report.xlsx")



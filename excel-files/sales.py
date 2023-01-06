import pandas as pd
from pathlib import Path

this_dir = Path(__file__).resolve().parent

parts = []
for path in (this_dir / "sales_data").rglob("*.xls*"):
    print(f'Reading {path.name}')
    part = pd.read_excel(path, index_col="transaction_id")
    parts.append(part)

df = pd.concat(parts)

pivot = pd.pivot_table(df, index="transaction_date", columns="store", values="amount", aggfunc="sum")

# Resample to end of month and assign an index name

summary = pivot.resample("M").sum()
summary.index.name = "Month"

# Write symmary report to Excel file

summary.to_excel(this_dir / "sales_report_pandas.xlsx")

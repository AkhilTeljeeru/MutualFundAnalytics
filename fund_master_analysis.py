import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("\nUnique Fund Houses")
print(df["fund_house"].nunique())

print(df["fund_house"].unique())

print("\nUnique Categories")
print(df["category"].unique())

print("\nUnique Sub Categories")
print(df["sub_category"].unique())

print("\nUnique Risk Grades")
print(df["risk_grade"].unique())
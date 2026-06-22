import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")
nav_history = pd.read_csv("data/raw/nav_history.csv")

master_codes = set(fund_master["scheme_code"])
nav_codes = set(nav_history["scheme_code"])

missing_codes = master_codes - nav_codes

print("=" * 60)
print("AMFI VALIDATION REPORT")
print("=" * 60)

print("Total Scheme Codes in Fund Master:", len(master_codes))
print("Total Scheme Codes in NAV History:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing Scheme Codes:")
    print(list(missing_codes)[:20])

coverage = (
    (len(master_codes) - len(missing_codes))
    / len(master_codes)
) * 100

print(f"\nCoverage: {coverage:.2f}%")

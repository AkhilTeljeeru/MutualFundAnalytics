import pandas as pd
import os

DATA_FOLDER = "data/raw"

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".csv"):

        file_path = os.path.join(DATA_FOLDER, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 80)
            print(f"FILE: {file}")
            print("=" * 80)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

            print("\nDuplicate Rows:")
            print(df.duplicated().sum())

        except Exception as e:
            print(f"Error reading {file}: {e}")
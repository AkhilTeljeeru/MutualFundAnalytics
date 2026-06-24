import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

for file in os.listdir(raw_folder):

    if file.endswith(".csv"):

        df = pd.read_csv(
            os.path.join(raw_folder, file)
        )

        # Cleaning
        df = df.drop_duplicates()

        cleaned_file = file.replace(
            ".csv",
            "_clean.csv"
        )

        df.to_csv(
            os.path.join(
                processed_folder,
                cleaned_file
            ),
            index=False
        )

        print(f"Saved {cleaned_file}")
from sqlalchemy import create_engine
import pandas as pd
import os

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

processed_folder = "data/processed"

for file in os.listdir(processed_folder):

    if file.endswith(".csv"):

        df = pd.read_csv(
            os.path.join(processed_folder, file)
        )

        table_name = file.replace(".csv", "")

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {table_name}")
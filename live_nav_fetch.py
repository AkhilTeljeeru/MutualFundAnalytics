import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{fund_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved -> {file_name}")

    else:
        print(f"Failed for {fund_name}")
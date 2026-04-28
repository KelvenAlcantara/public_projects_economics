import pandas as pd
import requests

countries = ["BRA", "USA", "CHL", "DEU"]

indicators = {
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "NE.CON.GOVT.ZS": "gov_size",
    "NE.GDI.FTOT.ZS": "investment",
    "FP.CPI.TOTL.ZG": "inflation",
    "NE.TRD.GNFS.ZS": "trade_open"
}

start_year = 1990
end_year = 2024


def fetch(indicator):
    rows = []

    for country in countries:
        url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=1000"
        data = requests.get(url).json()

        if len(data) < 2:
            continue

        for entry in data[1]:
            val = entry["value"]
            if val is None:
                continue

            year = int(entry["date"])

            if start_year <= year <= end_year:
                rows.append({
                    "country": country,
                    "year": year,
                    indicator: val
                })

    return pd.DataFrame(rows)


dfs = []

for code, name in indicators.items():
    print(f"Baixando {name}...")
    df = fetch(code)
    df = df.rename(columns={code: name})
    dfs.append(df)

from functools import reduce

# INNER JOIN (consistência)
df = reduce(lambda l, r: pd.merge(l, r, on=["country", "year"], how="inner"), dfs)

# =========================
# FEATURE ENGINEERING
# =========================

df = df.sort_values(["country", "year"])

# lag múltiplo (muito melhor)
df["gdp_future"] = df.groupby("country")["gdp_growth"].shift(-1)
df["gov_lag1"] = df.groupby("country")["gov_size"].shift(1)
df["gov_lag2"] = df.groupby("country")["gov_size"].shift(2)

df = df.dropna()

# =========================
# EXPORT
# =========================

df.to_csv("dataset_econometria.csv", index=False)
df[df["country"] == "BRA"].to_csv("dataset_brasil_econometria.csv", index=False)

print("✅ Dataset econométrico pronto")
import requests
import pandas as pd
from pathlib import Path
import time

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)


# =========================
# MAPA DE AGREGADOS
# =========================
def get_agg_by_year(year):
    if year >= 2020:
        return 7060
    elif year >= 2012:
        return 1419
    elif year >= 2006:
        return 2938
    else:
        raise ValueError(f"Ano {year} fora do range")


# =========================
# FETCH POR ANO
# =========================
def fetch_year(year):
    agg = get_agg_by_year(year)

    print(f"\n{year} (AGG {agg})")

    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/{agg}/periodos/{year}01-{year}12/variaveis/63?localidades=N1[all]&classificacao=315[all]"

    r = requests.get(url)

    if r.status_code != 200:
        print(f"Erro {year}")
        return None

    data = r.json()

    if not data:
        print(f"Sem dados {year}")
        return None

    resultados = data[0]["resultados"]

    rows = []

    for r in resultados:
        categoria_dict = r["classificacoes"][0]["categoria"]

        cat_id = list(categoria_dict.keys())[0]
        cat_nome = list(categoria_dict.values())[0]

        serie = r["series"][0]["serie"]

        for date, value in serie.items():
            rows.append({
                "date": pd.to_datetime(date, format="%Y%m"),
                "year": int(date[:4]),
                "month": int(date[4:]),
                "category_id": cat_id,
                "category": cat_nome,
                "value": float(value) if value not in ["...", "-", ""] else None
            })

    df = pd.DataFrame(rows)

    return df


# =========================
# BUILD DATASET
# =========================
def build_dataset(start=2006, end=2025):
    dfs = []

    for year in range(start, end + 1):
        df = fetch_year(year)

        if df is not None:
            dfs.append(df)

        time.sleep(0.3)

    final = pd.concat(dfs, ignore_index=True)

    return final


# =========================
# LIMPEZA (GRUPOS PRINCIPAIS)
# =========================
def filter_main_groups(df):
    grupos = [
        "Alimentação e bebidas",
        "Habitação",
        "Transportes",
        "Saúde e cuidados pessoais",
        "Educação",
        "Comunicação"
    ]

    df["group"] = df["category"].str.extract(r"^\d+\.(.*)")

    df_main = df[df["group"].isin(grupos)]

    return df_main


# =========================
# SAVE
# =========================
def save():
    df = build_dataset()

    df.to_csv(DATA_PATH / "ipca_full_raw.csv", index=False)

    df_main = filter_main_groups(df)

    df_main.to_csv(DATA_PATH / "ipca_main_groups.csv", index=False)

    yearly = df_main.groupby(["year", "group"])["value"].sum().reset_index()

    yearly.to_csv(DATA_PATH / "ipca_main_yearly.csv", index=False)

    print("\nPipeline finalizado!")
    print(df_main.head())


# =========================
# RUN
# =========================
if __name__ == "__main__":
    save()
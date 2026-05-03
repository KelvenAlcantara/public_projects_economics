import pandas as pd
import requests
import urllib3
import time
import numpy as np

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("\n===== PUSH FINAL DATAFRAME =====\n")


# =========================================================
# LOGGER
# =========================================================

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")


# =========================================================
# WORLD BANK
# =========================================================

def wb_fetch(indicator, name):
    log(f"WB: {name}")

    url = f"https://api.worldbank.org/v2/country/BRA/indicator/{indicator}?date=2000:2014&format=json"

    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        raise Exception(f"Erro WB: {name}")

    data = r.json()

    df = pd.DataFrame(data[1])[['date', 'value']]
    df.rename(columns={'date': 'ano', 'value': name}, inplace=True)

    df['ano'] = df['ano'].astype(int)

    return df


# =========================================================
# BANCO CENTRAL (INFLAÇÃO)
# =========================================================

def get_bcb():
    log("BCB: inflação")

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"

    r = requests.get(url, timeout=20)
    df = pd.DataFrame(r.json())

    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    df['ano'] = df['data'].dt.year

    df = df.groupby('ano')['valor'].mean().reset_index()
    df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

    df.rename(columns={'valor': 'inflacao'}, inplace=True)

    return df


# =========================================================
# IPEA UNIVERSAL
# =========================================================

def ipea_fetch(code, name):
    log(f"IPEA: {name}")

    try:
        url = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{code}')"
        r = requests.get(url, timeout=15)

        data = r.json()
        df = pd.DataFrame(data.get('value', []))

        if df.empty:
            raise Exception("DataFrame vazio")

        cols = df.columns

        # formato 1
        if 'VALDATA' in cols:
            df['data'] = pd.to_datetime(df['VALDATA'], utc=True)
            df['valor'] = pd.to_numeric(df['VALVALOR'], errors='coerce')

            df['ano'] = df['data'].dt.year
            df = df.groupby('ano')['valor'].mean().reset_index()

        # formato 2
        elif 'ANO' in cols:
            df.rename(columns={'ANO': 'ano', 'VALOR': 'valor'}, inplace=True)
            df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

        else:
            raise Exception(f"Formato desconhecido: {cols}")

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        df.rename(columns={'valor': name}, inplace=True)

        return df

    except Exception as e:
        log(f"[ERRO] {name}: {e}")
        return None


# =========================================================
# EXECUÇÃO
# =========================================================

gini = wb_fetch("SI.POV.GINI", "gini")
pib = wb_fetch("NY.GDP.PCAP.KD", "pib_per_capita")
export = wb_fetch("NE.EXP.GNFS.ZS", "export_pct_gdp")

inflacao = get_bcb()

ipea_pib = ipea_fetch("BM12_PIB12", "pib_ipea")
social = ipea_fetch("DFASPRE", "gasto_social")


# =========================================================
# MERGE FINAL
# =========================================================

log("Fazendo merge final")

df = gini.merge(pib, on='ano', how='left')
df = df.merge(inflacao, on='ano', how='left')

if ipea_pib is not None:
    df = df.merge(ipea_pib, on='ano', how='left')

if social is not None:
    df = df.merge(social, on='ano', how='left')

df = df.merge(export, on='ano', how='left')

df = df.sort_values('ano')


# =========================================================
# TRATAMENTO FINAL
# =========================================================

log("Checando NaNs...")
print(df.isna().sum())

# remover linhas sem Gini (variável dependente)
df = df.dropna(subset=['gini'])

# transformação log (opcional, útil pra regressão)
df['log_pib'] = np.log1p(df['pib_per_capita'])
df['log_social'] = np.log1p(df['gasto_social'])

# salvar
df.to_csv("../data/df_final.csv", index=False)

print("\n===== DATAFRAME FINAL =====\n")
print(df.head())

log("CSV salvo em ../data/df_final.csv")
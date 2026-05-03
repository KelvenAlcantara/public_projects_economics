import pandas as pd
import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("\n===== DEBUG COMPLETO EXPANDIDO =====\n")


# =========================================================
# LOGGER
# =========================================================

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")


def validate_df(df, name):
    if df is None:
        log(f"[ERRO] {name}: None")
        return False
    if df.empty:
        log(f"[ERRO] {name}: vazio")
        return False
    log(f"[OK] {name}: {len(df)} linhas")
    print(df.head(2), "\n")
    return True


# =========================================================
# 1. GINI (WORLD BANK)
# =========================================================

def test_gini():
    log("WB: Gini")

    url = "https://api.worldbank.org/v2/country/BRA/indicator/SI.POV.GINI?date=2000:2014&format=json"

    try:
        r = requests.get(url, timeout=30)
        data = r.json()

        df = pd.DataFrame(data[1])[['date', 'value']]
        df.rename(columns={'date': 'ano', 'value': 'gini'}, inplace=True)
        df['ano'] = df['ano'].astype(int)

        return df

    except Exception as e:
        log(f"Erro Gini: {e}")
        return None


# =========================================================
# 2. PIB (WORLD BANK)
# =========================================================

def test_world_bank():
    log("WB: PIB")

    url = "https://api.worldbank.org/v2/country/BRA/indicator/NY.GDP.PCAP.KD?date=2000:2014&format=json"

    try:
        r = requests.get(url, timeout=30)
        data = r.json()

        df = pd.DataFrame(data[1])[['date', 'value']]
        df.rename(columns={'date': 'ano', 'value': 'pib_per_capita'}, inplace=True)
        df['ano'] = df['ano'].astype(int)

        return df

    except Exception as e:
        log(f"Erro WB: {e}")
        return None


# =========================================================
# 3. INFLAÇÃO (BCB)
# =========================================================

def test_bcb():
    log("BCB: inflação")

    try:
        url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
        r = requests.get(url, timeout=10)

        df = pd.DataFrame(r.json())

        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

        df['ano'] = df['data'].dt.year
        df = df.groupby('ano')['valor'].mean().reset_index()

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        return df

    except Exception as e:
        log(f"Erro BCB: {e}")
        return None


# =========================================================
# 4. IPEA PIB
# =========================================================

def test_ipea_pib():
    log("IPEA: PIB")

    try:
        url = "http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='BM12_PIB12')"
        r = requests.get(url, timeout=10)

        df = pd.DataFrame(r.json().get('value', []))

        df['data'] = pd.to_datetime(df['VALDATA'], utc=True)
        df['valor'] = pd.to_numeric(df['VALVALOR'], errors='coerce')

        df['ano'] = df['data'].dt.year
        df = df.groupby('ano')['valor'].mean().reset_index()

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        return df

    except Exception as e:
        log(f"Erro IPEA PIB: {e}")
        return None


# =========================================================
# 5. IPEA SOCIAL (DFASPRE)
# =========================================================

def test_social():
    log("IPEA: gasto social")

    try:
        url = "http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='DFASPRE')"
        r = requests.get(url, timeout=10)

        df = pd.DataFrame(r.json().get('value', []))

        df['data'] = pd.to_datetime(df['VALDATA'], utc=True)
        df['valor'] = pd.to_numeric(df['VALVALOR'], errors='coerce')

        df['ano'] = df['data'].dt.year
        df = df.groupby('ano')['valor'].mean().reset_index()

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        return df

    except Exception as e:
        log(f"Erro social: {e}")
        return None


# =========================================================
# 6. SALÁRIO MÍNIMO (IPEA)
# =========================================================

def test_salario_min():
    log("IPEA: salário mínimo")

    try:
        url = "http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='PRECOS12_SALMINRE')"
        r = requests.get(url, timeout=10)

        df = pd.DataFrame(r.json().get('value', []))

        df['data'] = pd.to_datetime(df['VALDATA'], utc=True)
        df['valor'] = pd.to_numeric(df['VALVALOR'], errors='coerce')

        df['ano'] = df['data'].dt.year
        df = df.groupby('ano')['valor'].mean().reset_index()

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        return df

    except Exception as e:
        log(f"Erro salário mínimo: {e}")
        return None


# =========================================================
# 7. DESEMPREGO (IPEA)
# =========================================================

def test_desemprego():
    log("IPEA: desemprego")

    try:
        url = "http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='PNAD12_TXDESOC12')"
        r = requests.get(url, timeout=10)

        df = pd.DataFrame(r.json().get('value', []))

        df['data'] = pd.to_datetime(df['VALDATA'], utc=True)
        df['valor'] = pd.to_numeric(df['VALVALOR'], errors='coerce')

        df['ano'] = df['data'].dt.year
        df = df.groupby('ano')['valor'].mean().reset_index()

        df = df[(df['ano'] >= 2000) & (df['ano'] <= 2014)]

        return df

    except Exception as e:
        log(f"Erro desemprego: {e}")
        return None


# =========================================================
# 8. EXPORTAÇÕES (WORLD BANK)
# =========================================================

def test_exports():
    log("WB: exportações")

    url = "https://api.worldbank.org/v2/country/BRA/indicator/NE.EXP.GNFS.ZS?date=2000:2014&format=json"

    try:
        r = requests.get(url, timeout=30)
        data = r.json()

        df = pd.DataFrame(data[1])[['date', 'value']]
        df.rename(columns={'date': 'ano', 'value': 'export_pct_gdp'}, inplace=True)

        df['ano'] = df['ano'].astype(int)

        return df

    except Exception as e:
        log(f"Erro exportações: {e}")
        return None


# =========================================================
# EXECUÇÃO
# =========================================================

gini = test_gini()
validate_df(gini, "GINI")

wb = test_world_bank()
validate_df(wb, "PIB")

bcb = test_bcb()
validate_df(bcb, "INFLAÇÃO")

ipea_pib = test_ipea_pib()
validate_df(ipea_pib, "PIB IPEA")

social = test_social()
validate_df(social, "GASTO SOCIAL")

exp = test_exports()
validate_df(exp, "EXPORTAÇÕES")


# =========================================================
# CHECK FINAL
# =========================================================

log("Verificando integridade geral...")

datasets = [gini, wb, bcb, ipea_pib, social, exp]

if all(d is not None for d in datasets):
    log("✅ PIPELINE COMPLETO PRONTO")
else:
    log("⚠️ ALGUMAS SÉRIES FALHARAM")


log("Validando estrutura final esperada...")

expected_vars = {
    "gini",
    "pib_per_capita",
    "valor",  # inflacao antes de renomear
}

# checar manualmente cada DF
checks = {
    "gini": gini,
    "pib": wb,
    "inflacao": bcb,
    "pib_ipea": ipea_pib,
    "gasto_social": social,
    "export": exp
}

for name, d in checks.items():
    if d is not None:
        if 'ano' not in d.columns:
            log(f"[ERRO] {name} sem coluna ano")

log("✔ Estrutura básica validada")
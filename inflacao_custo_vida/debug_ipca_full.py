import requests

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
        raise ValueError("Ano fora do range suportado")


# =========================
# DEBUG METADADOS
# =========================
def debug_metadata(agg):
    print(f"\nMETADADOS (AGG {agg})\n")

    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/{agg}/metadados"
    meta = requests.get(url).json()

    print("Nome:", meta["nome"])

    print("\nVariáveis:")
    for v in meta["variaveis"]:
        print(f"   {v['id']} - {v['nome']}")

    print("\nClassificações:")
    for c in meta["classificacoes"]:
        print(f"\n{c['id']} - {c['nome']}")
        for cat in c["categorias"][:10]:
            print(f"   {cat['id']} - {cat['nome']}")


# =========================
# DEBUG DADOS
# =========================
def debug_data(year):
    agg = get_agg_by_year(year)

    print(f"\nDEBUG DADOS {year} (AGG {agg})\n")

    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/{agg}/periodos/{year}01-{year}12/variaveis/63?localidades=N1[all]&classificacao=315[all]"

    r = requests.get(url)

    print("Status:", r.status_code)

    data = r.json()

    if not data:
        print("Nenhum dado retornado")
        return

    print("\nQtd variáveis:", len(data))

    v = data[0]

    print("\nVariável:", v["variavel"])

    resultados = v["resultados"]

    print("\nQtd categorias:", len(resultados))

    print("\nExemplo de categoria:")
    exemplo = resultados[0]

    print("Classificação:", exemplo["classificacoes"])
    print("Campos:", exemplo["series"][0].keys())


# =========================
# TESTES MULTI-ANOS
# =========================
def run_debug():
    for year in [2010, 2014, 2018, 2022]:
        try:
            agg = get_agg_by_year(year)

            debug_metadata(agg)
            debug_data(year)

        except Exception as e:
            print(f"\nErro no ano {year}: {e}")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    run_debug()
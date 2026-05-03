Autor: Kelven de Alcantara Bonfim

Data: 02/05/2026

# 📚 Fundamentação Teórica

A queda da desigualdade de renda no Brasil entre 2001 e 2014 pode ser compreendida a partir da interação entre diferentes mecanismos econômicos e institucionais. Esta seção apresenta os principais canais explicativos.

---

## Transferência de Renda

Programas de transferência direta, como o **Bolsa Família**, atuam reduzindo a desigualdade de forma imediata ao:

- Aumentar a renda das camadas mais pobres
- Reduzir a pobreza extrema
- Elevar o consumo básico

Esses programas têm efeito direto no Gini, pois impactam a base da distribuição de renda.

---

## Crescimento Econômico

O crescimento econômico pode reduzir a desigualdade quando:

- Gera empregos formais
- Aumenta salários reais
- Expande oportunidades produtivas

No período analisado, o crescimento foi acompanhado por inclusão no mercado de trabalho, ampliando a renda das classes mais baixas.

---

## Mercado de Trabalho

Mesmo sem dados diretos neste modelo, o mercado de trabalho é um canal central:

- Queda do desemprego
- Formalização do emprego
- Valorização do salário mínimo

Esses fatores contribuem para uma compressão da distribuição de renda.

---

## Choques Externos

O ambiente internacional teve papel relevante:

- Boom das commodities
- Aumento das exportações
- Entrada de divisas

Isso fortaleceu o crescimento interno e ampliou a capacidade fiscal do Estado.

---

## Interação dos Fatores

Os mecanismos não atuam isoladamente. A redução da desigualdade resulta da combinação de:

- Crescimento econômico favorável
- Expansão do gasto social
- Contexto externo positivo

---

## Implicação Teórica

A desigualdade não responde a um único vetor causal, mas a um **equilíbrio macroeconômico específico**, onde políticas públicas e condições econômicas se reforçam mutuamente.

---
# 📊 Descrição dos Dados

Esta etapa apresenta as variáveis utilizadas no modelo empírico, suas origens e o papel analítico de cada uma.



## Estrutura do Dataset

O dataset é composto por observações anuais entre **2001 e 2014**, contendo indicadores macroeconômicos e sociais relevantes para explicar a dinâmica da desigualdade no Brasil.

---

## Variáveis Utilizadas

### Índice de Gini (`gini`)
- Mede a desigualdade de renda
- Varia de 0 a 100
- **Variável dependente (Y)** do modelo

---

### PIB per capita (`pib_per_capita`)
- Proxy do nível de renda média da população
- Captura efeitos de crescimento econômico sobre a desigualdade

---

### Inflação (`inflacao`)
- Mede a variação média de preços
- Afeta principalmente as camadas mais pobres
- Pode aumentar a desigualdade se elevada

---

### PIB (IPEA) (`pib_ipea`)
- Medida agregada da atividade econômica
- Usada como proxy alternativa de crescimento

---

### Gasto Social (`gasto_social`)
- Representa despesas públicas com políticas sociais
- Proxy para redistribuição de renda via Estado

---

### Exportações (% do PIB) (`export_pct_gdp`)
- Mede a relevância do setor externo
- Proxy para o efeito do boom de commodities
- Captura choques externos positivos

---

### Transformações Logarítmicas

#### `log_pib`
- Logaritmo do PIB (IPEA)
- Reduz escala e melhora propriedades estatísticas

#### `log_social`
- Logaritmo do gasto social
- Permite interpretar efeitos proporcionais

---

## Papel das Variáveis no Modelo

| Tipo                | Variável              | Função |
|---------------------|----------------------|--------|
| Dependente          | Gini                 | Medir desigualdade |
| Crescimento         | PIB / PIB per capita | Capturar efeito econômico |
| Política pública    | Gasto social         | Medir redistribuição |
| Setor externo       | Exportações          | Capturar contexto global |
| Estabilidade macro  | Inflação             | Controle econômico |

---

## Observação Importante

O número de observações é limitado devido à disponibilidade de dados do Gini, o que impõe restrições na robustez estatística dos resultados.


# Resultado
Abordado e aprofundado no arquivo RESULTS.md
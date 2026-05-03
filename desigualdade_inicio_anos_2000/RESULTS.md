## Resultados Empíricos — Desigualdade no Brasil (2001–2014)

---

## 1. Fato Estilizado

A análise inicial confirma uma tendência clara e robusta de redução da desigualdade de renda no Brasil entre 2001 e 2014.

* O índice de Gini apresenta queda contínua ao longo do período
* Pequenas reversões pontuais não alteram a tendência estrutural
* A redução é consistente e de magnitude relevante

Esse comportamento é visível na série temporal apresentada no projeto 

**Conclusão:**
A queda da desigualdade é um fenômeno empírico sólido e não controverso.

---

## 2. Relações Empíricas (Correlação)

A matriz de correlação revela relações fortes entre o Gini e variáveis macroeconômicas:

* Log PIB: **-0.98**
* Log Gasto Social: **-0.97**
* Exportações (% PIB): **+0.68**
* Inflação: **+0.56** 

Além disso:

* Correlação entre log PIB e log gasto social: **0.996**

---

### Interpretação

* Crescimento econômico e gasto social estão fortemente associados à queda da desigualdade
* Existe **multicolinearidade extrema** entre PIB e gasto social
* Exportações apresentam relação positiva com Gini, indicando comportamento distinto

---

## 3. Modelo Base (OLS em Níveis)

O modelo linear com variáveis em nível apresenta:

* R²: **0.976**
* Nenhuma variável significativa individualmente
* Condição numérica elevada (indicando multicolinearidade) 

---

### Interpretação

Apesar do alto poder explicativo agregado:

* O modelo não consegue identificar efeitos individuais
* Os coeficientes são instáveis
* A inferência causal é comprometida

**Diagnóstico:** presença de multicolinearidade estrutural.

---

## 4. Modelo com Crescimento (V2)

Ao utilizar taxas de crescimento:

* R²: **0.827**
* Apenas exportações aparecem significativas (p < 0.01)
* PIB e gasto social não são estatisticamente significativos 

---

### Interpretação

* A transformação reduz o problema de tendência espúria
* Ainda persiste dificuldade de identificação dos efeitos
* Evidência de que o modelo linear simples é insuficiente

---

## 5. Modelo com Interação (Estado + Mercado)

Introdução da variável:

```
estado_mercado = log_pib × log_social
```

Resultados:

* R²: **0.961**
* Variável de interação altamente significativa (p < 0.001)
* Variáveis isoladas permanecem não significativas 

---

### Interpretação

* O efeito relevante não é individual, mas **conjunto**
* Crescimento e gasto social atuam de forma complementar
* O modelo melhora substancialmente ao capturar interação

**Insight central:**
A redução da desigualdade está associada à combinação entre expansão econômica e capacidade fiscal.

---

## 6. Análise por Períodos

### 6.1 Período de crescimento (2001–2008)

* R² elevado (~0.93)
* Baixa significância estatística
* Amostra pequena limita inferência 

### 6.2 Pós-crise (2009–2014)

* Modelo perde validade estatística
* Grau de liberdade insuficiente
* Overfitting evidente

---

### Interpretação

* A dinâmica muda após 2008
* Modelos lineares tornam-se menos confiáveis
* Evidência de mudança estrutural no período

---

## 7. Causalidade Temporal (Granger)

Resultados:

### PIB → Gini

* p = 0.014 (lag 1)

### Gasto Social → Gini

* p = 0.030 (lag 1) 

---

### Interpretação

* Há evidência de precedência temporal
* Crescimento e gasto social antecedem variações no Gini
* Não implica causalidade estrutural forte, mas reforça direção temporal

---

## 8. Modelo Dinâmico (VAR)

### Equação do Gini:

* dlog_pib (lag 1): significativo (p = 0.006)
* dlog_social (lag 1): significativo (p = 0.022) 

---

### Interpretação

* Choques em crescimento e gasto social impactam a desigualdade
* O efeito ocorre com defasagem temporal
* A dinâmica é consistente com mecanismos econômicos reais

---

## 9. Função Impulso-Resposta (IRF)

A análise dinâmica mostra:

* Impactos não imediatos sobre o Gini
* Respostas graduais ao longo do tempo
* Dissipação dos efeitos após alguns períodos 

---

### Interpretação

* A desigualdade responde como variável de ajuste
* O sistema apresenta propagação temporal
* Reforça natureza dinâmica do fenômeno

---

## 10. Decomposição de Variância (FEVD)

Resultados indicam:

* Forte componente autoregressivo do Gini
* Contribuição relevante de PIB e gasto social
* Influência distribuída ao longo do tempo 

---

### Interpretação

* A desigualdade possui inércia significativa
* Mas responde a choques macroeconômicos
* O fenômeno não é puramente estrutural nem totalmente reativo

---

## 11. Modelo ARDL

Resultados:

* Gini defasado altamente significativo (~0.93)
* PIB e gasto social não significativos 

---

### Interpretação

* Forte dependência temporal (path dependence)
* Curto prazo dominado por inércia
* Efeitos macroeconômicos são difusos

---

## 12. Síntese Geral

A evidência empírica aponta para um padrão consistente:

1. A desigualdade caiu de forma estrutural no período
2. Crescimento e gasto social apresentam forte associação com o Gini
3. Existe multicolinearidade entre variáveis-chave
4. Modelos lineares simples não capturam adequadamente o fenômeno
5. A interação entre variáveis melhora substancialmente o ajuste
6. Há evidência de precedência temporal (Granger)
7. A dinâmica mostra efeitos propagados no tempo

---

## 13. Conclusão Principal

A queda da desigualdade no Brasil entre 2001 e 2014 não pode ser atribuída a um único fator.

Os resultados indicam que o fenômeno é melhor explicado como:

> Um processo sistêmico resultante do alinhamento entre crescimento econômico, expansão do gasto social e condições externas favoráveis.

---

## 14. Implicações

* Explicações unidimensionais são insuficientes
* Modelos ideológicos simplificados não capturam a realidade empírica
* A interação entre variáveis macroeconômicas é central
* A desigualdade deve ser analisada como fenômeno dinâmico

---

## 15. Limitações

* Amostra pequena (13 observações)
* Alto risco de multicolinearidade
* Limitações de inferência causal
* Sensibilidade a especificação de modelo

---

## 16. Direções Futuras

* Expansão da base temporal
* Inclusão de variáveis institucionais
* Modelos estruturais (SVAR)
* Análise comparativa internacional

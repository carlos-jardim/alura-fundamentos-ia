# 1. Criando a Rede Bayesiana
probabilidades = {
    "HistoricoCompras": {0: 0.7, 1: 0.3},  # 0: Não tem histórico, 1: Tem histórico
    "TempoNoSite": {0: 0.6, 1: 0.4},       # 0: Pouco tempo, 1: Muito tempo
    "ClicouEmPromocao": {0: 0.8, 1: 0.2},  # 0: Não clicou, 1: Clicou
    "Compra": {
        (0, 0, 0): 0.1,  # Não tem histórico, pouco tempo, não clicou
        (0, 0, 1): 0.3,  # Não tem histórico, pouco tempo, clicou
        (0, 1, 0): 0.2,  # Não tem histórico, muito tempo, não clicou
        (0, 1, 1): 0.6,  # Não tem histórico, muito tempo, clicou
        (1, 0, 0): 0.4,  # Tem histórico, pouco tempo, não clicou
        (1, 0, 1): 0.7,  # Tem histórico, pouco tempo, clicou
        (1, 1, 0): 0.8,  # Tem histórico, muito tempo, não clicou
        (1, 1, 1): 0.9   # Tem histórico, muito tempo, clicou
    }
}

# 2. Função para calcular a probabilidade conjunta de compra
def calcular_probabilidade_compra(evidencias):
    historico = evidencias["HistoricoCompras"]
    tempo = evidencias["TempoNoSite"]
    promocao = evidencias["ClicouEmPromocao"]

    prob_compra = probabilidades["Compra"][(historico, tempo, promocao)]
    prob_nao_compra = 1 - prob_compra

    return {"Comprar": prob_compra, "Não Comprar": prob_nao_compra}

# 3. Testando com o cenário descrito
evidencias = {
    "HistoricoCompras": 1,  # Cliente tem histórico de compras
    "TempoNoSite": 0,       # Cliente passou pouco tempo no site
    "ClicouEmPromocao": 1   # Cliente clicou em promoções
}

resultados = calcular_probabilidade_compra(evidencias)
print("Probabilidades de Compra:")
for resultado, probabilidade in resultados.items():
    print(f"{resultado}: {probabilidade:.2f}")

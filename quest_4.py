# valor de faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcula o valor total mensal
valor_total = sum(faturamento_mensal.values())

# calcula o percentual de representação de cada estado
percentuais = {}
for estado, faturamento in faturamento_mensal.items():
    percentuais[estado] = faturamento / valor_total * 100

# imprime os percentuais de representação de cada estado
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')

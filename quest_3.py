import json

# Abrir o arquivo JSON e carregar os dados em um dicionário
with open("C:/Users/ildo_/Documents/json/faturamento.json", "r") as f:
    faturamento = json.load(f)

# Inicializar as variáveis
menor_valor = float('inf')  # infinito positivo
maior_valor = float('-inf')  # infinito negativo
soma_valores = 0
dias_acima_media = 0

# Percorrer o dicionário de faturamento
for dia, valor in faturamento.items():
    # Ignorar dias sem faturamento (valores vazios)
    if valor:
        valor_float = float(valor)
        soma_valores += valor_float
        # Atualizar o menor e o maior valor de faturamento
        if valor_float < menor_valor:
            menor_valor = valor_float
        if valor_float > maior_valor:
            maior_valor = valor_float

# Calcular a média mensal de faturamento (ignorando dias sem faturamento)
media_mensal = soma_valores / len(faturamento)

# Percorrer o dicionário de faturamento novamente para contar os dias acima da média
for valor in faturamento.values():
    if valor:
        if float(valor) > media_mensal:
            dias_acima_media += 1

# Imprimir os resultados
print("Menor valor de faturamento: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento: R$ {:.2f}".format(maior_valor))
print("{} dias tiveram valor de faturamento acima da média mensal de R$ {:.2f}".format(dias_acima_media, media_mensal))


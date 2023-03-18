# Recebe a string a ser invertida
texto = input("Digite o texto a ser invertido: ")

# Inicializa uma string vazia para armazenar o texto invertido
invertido = ""

# Itera sobre os caracteres da string, de trás para frente
for i in range(len(texto)-1, -1, -1):
    invertido += texto[i]

# Imprime o texto invertido
print("O texto invertido é:", invertido)

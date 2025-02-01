import random

# Nome do arquivo de saída
nome_arquivo = 'Arquivos/arq03.txt'

# Gera uma lista com 10.000 números inteiros aleatórios entre 1 e 100.000
numeros = [random.randint(1, 100000) for _ in range(100000)]

# Escreve os números no arquivo, um por linha
with open(nome_arquivo, 'w') as arquivo:
    for numero in numeros:
        arquivo.write(f"{numero}\n")

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
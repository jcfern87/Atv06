def ler_numeros_de_arquivo(nome_arquivo):
    # Lista para armazenar os números
    numeros = []
    
    # Abre o arquivo no modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê cada linha do arquivo
        for linha in arquivo:
            # Remove espaços em branco e converte a linha para um número
            numero = int(linha.strip())
            # Adiciona o número à lista
            numeros.append(numero)
    
    return numeros

def salva_arquivo(array, arq_saida):
    # Salva o array ordenado em um arquivo txt
	with open(arq_saida, 'w') as arquivo_res:
		for number in array:
			arquivo_res.write(f"{number}\n")
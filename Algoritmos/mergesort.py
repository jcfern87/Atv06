import lerarquivo
import time


def mergeSort(arr):
    # Caso base: se a lista tiver 0 ou 1 elemento, já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Divide a lista ao meio
    meio = len(arr) // 2
    esquerda = arr[:meio]  # Sublista da esquerda
    direita = arr[meio:]   # Sublista da direita
    
    # Recursivamente ordena as sublistas
    esquerda = mergeSort(esquerda)
    direita = mergeSort(direita)
    
    # Combina (merge) as sublistas ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []  # Lista para armazenar o resultado combinado
    i = j = 0       # Índices para percorrer as sublistas esquerda e direita
    
    # Combina as sublistas ordenadas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes da sublista esquerda (se houver)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    # Adiciona os elementos restantes da sublista direita (se houver)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado


# Medição do tempo
inicio = time.time()

# Leitura do arquivo por meio de import
array = lerarquivo.ler_numeros_de_arquivo("Arquivos/arq03.txt")
arquivo_saida = "Resultados/resultadosmerge.txt"
array_ord = mergeSort(array)
lerarquivo.salva_arquivo(array_ord, arquivo_saida)
print(f"Arquivo '{arquivo_saida}') criado com os números ordenados.")

fim = time.time()

tempo_decorrido = (fim - inicio) * 1000
print(f"Tempo de execução do Merge Sort: {tempo_decorrido:.3f} ms")





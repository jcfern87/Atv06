import lerarquivo, time

def quickSort(arr):
    # Caso base: se a lista tiver 0 ou 1 elemento, já está ordenada
    if len(arr) <= 1:
        return arr
    
    # Escolhe o pivô (neste caso, o último elemento da lista)
    pivô = arr[-1]
    
    # Particiona a lista em três partes:
    # - Elementos menores que o pivô
    # - Elementos iguais ao pivô
    # - Elementos maiores que o pivô
    menores = [x for x in arr[:-1] if x < pivô]
    iguais = [x for x in arr if x == pivô]
    maiores = [x for x in arr[:-1] if x > pivô]
    
    # Recursivamente ordena as sublistas de menores e maiores
    return quickSort(menores) + iguais + quickSort(maiores)

inicio = time.time()

# Leitura do arquivo por meio de import
array = lerarquivo.ler_numeros_de_arquivo("Arquivos/arq03.txt")
arquivo_saida = "Resultados/resultadosquick.txt"

array_ord = quickSort(array)

lerarquivo.salva_arquivo(array_ord, arquivo_saida)
print(f"Arquivo '{arquivo_saida}') criado com os números ordenados.")

fim = time.time()

tempo_decorrido = (fim - inicio) * 1000
print(f"Tempo de execução do Quick Sort: {tempo_decorrido:.3f} ms")

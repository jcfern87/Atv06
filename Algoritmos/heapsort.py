import lerarquivo, heapq, time

# Function to perform the sorting using
# heaop sort
def heap_sort(arr):
	heapq.heapify(arr)
	result = []
	while arr:
		result.append(heapq.heappop(arr))
	return result

# Medição do tempo
inicio = time.time()

# Leitura do arquivo por meio de import
array = lerarquivo.ler_numeros_de_arquivo("Arquivos/arq03.txt")
arquivo_saida = "Resultados/resultadosheap.txt"
array_ord = heap_sort(array)
lerarquivo.salva_arquivo(array_ord, arquivo_saida)
print(f"Arquivo '{arquivo_saida}') criado com os números ordenados.")

fim = time.time()

tempo_decorrido = (fim - inicio) * 1000
print(f"Tempo de execução do Merge Sort: {tempo_decorrido:.3f} ms")

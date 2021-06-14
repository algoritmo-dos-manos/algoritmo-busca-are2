import random, insertion_sort, quick_sort, selection_sort

def ordenacaos(lista):
    insertion_sort.insertion_sort(lista)
    quick_sort.quick_sort(lista)
    selection_sort.selection_sort(lista)
    print(f'{insertion_sort.comparacoes_insertion_sort} - Insertion Sort.')
    print(f'{quick_sort.comparacoes_quick_sort} - Quick Sort.')
    print(f'{selection_sort.comparacao_selection_sort} - Selection Sort.')
    insertion_sort.limpar_comparacoes()
    quick_sort.limpar_comparacoes()
    selection_sort.limpar_comparacoes()

# Define listas com os numeros aleatorios:
tamanho = 10
lista_de_numeros_10 = random.sample(range(0, tamanho * 10), tamanho)
tamanho = 50
lista_de_numeros_50 = random.sample(range(0, tamanho * 10), tamanho)
tamanho = 100
lista_de_numeros_100 = random.sample(range(0, tamanho * 10), tamanho)
tamanho = 1000
lista_de_numeros_1000 = random.sample(range(0, tamanho * 10), tamanho)

print('Vetor 10:')
ordenacaos(lista_de_numeros_10)
print('..............')
print('Vetor 50:')
ordenacaos(lista_de_numeros_50)
print('..............')
print('Vetor 100:')
ordenacaos(lista_de_numeros_100)
print('..............')
print('Vetor 1000:')
ordenacaos(lista_de_numeros_1000)





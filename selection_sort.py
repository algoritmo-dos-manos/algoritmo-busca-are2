
comparacao_selection_sort = 0

def limpar_comparacoes():
    global comparacao_selection_sort
    comparacao_selection_sort = 0

def encontrar_menor_elemento(lista):
    global comparacao_selection_sort
    indice_menor_elemento = 0
    menor_elemento = lista[indice_menor_elemento]

    for i, elemento in enumerate(lista[1:], start = 1):
        comparacao_selection_sort += 1
        if (elemento < menor_elemento):
            menor_elemento = elemento
            indice_menor_elemento = i

    return indice_menor_elemento

# Função Selection Sort 
def selection_sort(lista_desordenada_):
    global comparacao_selection_sort
    lista_ordenada = []
    lista_desordenada = lista_desordenada_.copy()
    list_tamanho = len(lista_desordenada)

    for i in range(list_tamanho):
        
        indice_menor_elemento = encontrar_menor_elemento(lista_desordenada)
        lista_ordenada.append(lista_desordenada.pop(indice_menor_elemento))

    return lista_ordenada
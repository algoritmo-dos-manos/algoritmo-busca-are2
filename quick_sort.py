# Função Quick sort
comparacoes_quick_sort = 0

def limpar_comparacoes():
    global comparacoes_quick_sort, trocas
    comparacoes_quick_sort = 0
    trocas = 0

def quick_sort(lista_):
    global comparacoes_quick_sort, trocas
    lista = lista_.copy()
    tamanho_do_vetor = len(lista)
    comparacoes_quick_sort += 1
    if tamanho_do_vetor <= 1:
        return lista
    else:
        pivot = lista.pop()

    maiores_numeros = []
    menores_numeros = []

    for numero in lista:
        comparacoes_quick_sort += 1
        
        if numero > pivot:
            maiores_numeros.append(numero)
        else:
            menores_numeros.append(numero)
    return quick_sort(menores_numeros) + [pivot] + quick_sort(maiores_numeros)
# Função insertion sort
comparacoes_insertion_sort = 0

def limpar_comparacoes():
    global comparacoes_insertion_sort
    comparacoes_insertion_sort = 0

def insertion_sort(lista_):
    index_1 = 1
    lista = lista_.copy()
    global comparacoes_insertion_sort
    while (index_1 < len(lista)):
        item_lista_temporario = lista[index_1]
        trocou = False
        index_2 = index_1- 1 # valida se o index_1 é menor que o index_2
        
        while (index_2 >=0 and lista[index_2] > item_lista_temporario):
            
            lista[index_2+1] = lista[index_2]
            trocou = True
            index_2 -= 1
        
        if (trocou):
            lista[index_2 + 1] = item_lista_temporario
        comparacoes_insertion_sort += 1
        index_1 += 1
    return lista
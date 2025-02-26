import random

def faz_remessa(G, tamanho_de_remessa, caracter):
    lista_de_remessa = []
    tamanho_do_cd = len(G.nodes)        
    lista_de_remessa = random.sample(range(tamanho_do_cd), tamanho_de_remessa)
    for i in range(tamanho_do_cd):
        if i % 100 == 0 or i % 100 == 45 or i % 100 == 73 or i % 100 == 99:
            if i in lista_de_remessa:
                lista_de_remessa.remove(i)
    lista_de_remessa = adiciona_esteira_na_remessa(G, lista_de_remessa, caracter)
    return lista_de_remessa

def faz_fila_de_remessas(G, tamanho_de_remessa, numero_de_remessas):
    fila_de_remessas = []
    for i in range(numero_de_remessas):
        if fila_de_remessas == []:
            fila_de_remessas.append(faz_remessa(G, tamanho_de_remessa, caracter = 0))
        else:
            fila_de_remessas.append(faz_remessa(G, tamanho_de_remessa, caracter = 1))
        

    return fila_de_remessas

def adiciona_esteira_na_remessa(G, lista_de_remessa, caracter):
    lista_de_remessa_com_esteira = []
    #existem 20 esteiras
    if caracter == 0:
        lista_de_remessa_com_esteira.append(random.choice(range(G.number_of_nodes()-20 , G.number_of_nodes()-1)))
    lista_de_remessa_com_esteira.extend(lista_de_remessa)
    lista_de_remessa_com_esteira.append(random.choice(range(G.number_of_nodes()-20 , G.number_of_nodes()-1)))
    return lista_de_remessa_com_esteira
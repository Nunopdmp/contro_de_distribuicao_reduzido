import networkx as nx
import random

def melhor_distancia(G, A, B):

    return nx.shortest_path_length(G, source=A, target=B, weight='weight')

def tamanho_medio_percorrido(G, repeticoes):
    distancia_total = 0
    validas = 0  # Contador de tentativas válidas
    for _ in range(repeticoes):
        A, B = random.sample(range(G.number_of_nodes()), 2)  # Garante A ≠ B
        dist = melhor_distancia(G, A, B)
        distancia_total += dist
        validas += 1

    return distancia_total / validas if validas > 0 else float('inf')
def vetor_de_distancia(G,lista_de_remessa):
    x = 0
    vetor_distancia_final = []
    for remessa in lista_de_remessa:
        vetor_distancia = []
        validas = 0  # Contador de tentativas válidas
        for i in range(len(remessa)-1):
            dist = melhor_distancia(G, remessa[i], remessa[i+1])
            vetor_distancia.append(dist)
            validas += 1
        vetor_distancia_final.append(vetor_distancia)
    return vetor_distancia_final if validas > 0 else float('inf')

def distancia_percorrida(vetor_de_distancia):
    soma = 0
    comprimento = 0
    for vetor_distancia in vetor_de_distancia:
        comprimento += len(vetor_distancia)
        for distancia in vetor_distancia:
            soma += distancia
    return soma, soma/comprimento

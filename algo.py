import networkx as nx
from itertools import permutations
import tamanho_medio_percorrido as tmp

def organizar_caminho(posicoes):
    # Organiza as posições por rua
    ruas = {}
    for pos in posicoes:
        rua = pos // 100  # Identifica a rua
        if rua not in ruas:
            ruas[rua] = []
        ruas[rua].append(pos)
    
    # Ordena as ruas
    ruas_ordenadas = sorted(ruas.keys())
    
    caminho = []
    sentido = True  # Define o sentido inicial (crescente)
    
    for rua in ruas_ordenadas:
        if sentido:
            caminho.extend(sorted(ruas[rua]))
        else:
            caminho.extend(sorted(ruas[rua], reverse=True))
        sentido = not sentido  # Alterna o sentido para a próxima rua
    
    return caminho


def algo_de_busca_de_caminho_bronco(fila_de_remessas):
    """Da esquerda para direita 
    sobe a primeira rua
    desce a segunda rua
    assim por diante
    """
    caminho = []
    remessa_temp = []
    posicao_de_esteira = 0
    x=0
    for remessa in fila_de_remessas:
        if x == 0: 
            posicao_de_esteira_inicial = remessa[0]
            posicao_de_esteira_final = remessa[-1]
            remessa = remessa[1:]
            remessa = remessa [:-1]
            remessa_temp.append(posicao_de_esteira_inicial)
            remessa_temp = remessa_temp + organizar_caminho(remessa)
            remessa_temp.append(posicao_de_esteira_final)
            caminho.append(remessa_temp)
            remessa_temp = []
            x=1 
        else:
            remessa = [posicao_de_esteira_final] + remessa
            posicao_de_esteira_inicial = remessa[0]
            posicao_de_esteira_final = remessa[-1]
            remessa = remessa[1:]
            remessa = remessa [:-1]
            remessa_temp.append(posicao_de_esteira_inicial)
            remessa_temp = remessa_temp + organizar_caminho(remessa)
            remessa_temp.append(posicao_de_esteira_final)
            caminho.append(remessa_temp)
            remessa_temp = []
    return caminho


def algo_de_busca_de_caminho_cinza(fila_de_remessas):
    """Sempre sobe as ruas
    independente do nº da rua
    """
    caminho = []
    remessa_temp = []
    posicao_de_esteira = 0
    x=0
    for remessa in fila_de_remessas:
        if x == 0: 
            posicao_de_esteira_inicial = remessa[0]
            posicao_de_esteira_final = remessa[-1]
            remessa = remessa[1:]
            remessa = remessa [:-1]
            remessa_temp.append(posicao_de_esteira_inicial)
            remessa_temp = remessa_temp + sorted(remessa)
            remessa_temp.append(posicao_de_esteira_final)
            caminho.append(remessa_temp)
            remessa_temp = []
            x=1 
        else:
            remessa = [posicao_de_esteira_final] + remessa
            posicao_de_esteira_inicial = remessa[0]
            posicao_de_esteira_final = remessa[-1]
            remessa = remessa[1:]
            remessa = remessa [:-1]
            remessa_temp.append(posicao_de_esteira_inicial)
            remessa_temp = remessa_temp + sorted(remessa)
            remessa_temp.append(posicao_de_esteira_final)
            caminho.append(remessa_temp)
            remessa_temp = []
    return caminho

def algo_de_busca_de_caminho_melhor_forca_bruta(G, fila_de_remessas):
    caminho = []
    remessa_temp = []
    x=0
    for remessa in fila_de_remessas:
        if x ==0:
            posicao_de_esteira_final = remessa[-1]
            caminho.append(melhor_caminho(G, remessa))
            x=1
        else:
            remessa = [posicao_de_esteira_final] + remessa
            posicao_de_esteira_final = remessa[-1]
            caminho.append(melhor_caminho(G, remessa))
    return caminho

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

def melhor_caminho(G, remessa):
    posi_inicial = remessa[0]
    posi_final = remessa[-1]
    remessa = remessa[1:]
    remessa = remessa[:-1]
    todas_permutacoes = permutations(remessa)
    custo_min = float('inf')
    for per in todas_permutacoes:
        per = list(per)
        per = [posi_inicial] + per + [posi_final]
        custo,_ = tmp.distancia_percorrida(vetor_de_distancia= tmp.vetor_de_distancia(G, [per]))
        if custo < custo_min:
            melhor_caminho = per
            custo_min = custo
    return melhor_caminho







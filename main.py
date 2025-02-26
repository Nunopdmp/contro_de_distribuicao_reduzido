import grapho
import networkx as nx
import matplotlib.pyplot as plt
import fila_remessas as fr
import algo
import tamanho_medio_percorrido as tmp

cd = nx.read_graphml("cd_controlado_esteiras.graphml")
cd = nx.relabel_nodes(cd, {n: int(n) for n in cd.nodes})
nx.set_edge_attributes(cd, 1, "weight")
print("\nCentro de Distribuições carregados ", cd)
fila = fr.faz_fila_de_remessas(cd, 7, 2)
print("\nFila de remessas criada ", fila)

print("\nA busca de compra bronca é ", algo.algo_de_busca_de_caminho_bronco(fila))
vetor_de_distancia = tmp.vetor_de_distancia(cd, algo.algo_de_busca_de_caminho_bronco(fila))
print("\nO vetor de distância é ", vetor_de_distancia)
distancia, media = tmp.distancia_percorrida(vetor_de_distancia)
print("\nA distância percorrida na separação bronca é ", distancia)
print("\nA média da distância percorrida na separação bronca é ", media)

print("\nA busca de compra cinza é ", algo.algo_de_busca_de_caminho_cinza(fila))
vetor_de_distancia = tmp.vetor_de_distancia(cd, algo.algo_de_busca_de_caminho_cinza(fila))
print("\nO vetor de distância é ", vetor_de_distancia)
distancia, media = tmp.distancia_percorrida(vetor_de_distancia)
print("\nA distância percorrida na separação cinza é ", distancia)
print("\nA média da distância percorrida na separação cinza é ", media)

melhor_caminho = algo.algo_de_busca_de_caminho_melhor_forca_bruta(cd,fila)
print("\nA busca de compra ótima é ",melhor_caminho)
vetor_de_distancia = tmp.vetor_de_distancia(cd, melhor_caminho)
print("\nO vetor de distância é ", vetor_de_distancia)
distancia, media = tmp.distancia_percorrida(vetor_de_distancia)
print("\nA distância percorrida na separação ótima é ", distancia)
print("\nA média da distância percorrida na separação ótima é ", media)


import sys
import networkx as nx

# Criar um grafo não direcionado
G = nx.Graph()
'''if len(sys.argv) != 4:
    print("Usage: python grapho.py <posicao> <ruas> <corredor>")
    sys.exit(1)'''

posicao = 100 #int(sys.argv[1])
ruas = 25 #int(sys.argv[2])
corredor = 3 #int(sys.argv[3])

def faz_ruas(G, posicao, ruas):
    for i in range(ruas):
        lista = list(range(i*posicao, (i+1)*posicao))
        G.add_nodes_from(lista)
        for i in range(len(lista)-1):
            G.add_edge(lista[i], lista[i+1])
    for i in range(len(G.nodes)-posicao):
        if i % 100 in {0, 45, 73, 99}:
            G.add_edge(i, i+posicao)
    return G

def adiciona_controlado(G, ruas_controlado: int, posicao_controlado = posicao):
    G_copy = G.copy()
    lista = range(G.number_of_nodes(), G.number_of_nodes() + ruas_controlado * posicao_controlado)
    G_copy.add_nodes_from(lista)
    for i in range(len(lista)-1):
        if i % posicao_controlado != 99:
            G_copy.add_edge(lista[i], lista[i+1])
    node_range = range(G.number_of_nodes(), G_copy.number_of_nodes()-posicao_controlado)
    for i in node_range:
        if i % 100 == 0 or i % 100 == 45 or i % 100 == 73 or i % 100 == 99:
            G_copy.add_edge(i, i + posicao_controlado)
    G_copy.add_edge(G.number_of_nodes()-posicao,G.number_of_nodes())
    return G_copy

def adiciona_esteiras(G, quantidade_esteiras = 20):
    G_copy = G.copy()
    for i in range(quantidade_esteiras*posicao):
        if i % posicao == 0:
            G_copy.add_node(G_copy.number_of_nodes())
            G_copy.add_edge(i, G_copy.number_of_nodes()-1)

    return G_copy

"""cd  = faz_ruas(G, 100 , 25)

cd_controlado = adiciona_controlado(cd, 5, 100)

cd_controlado_esteiras = adiciona_esteiras(cd_controlado)

nx.write_graphml(cd, "cd.graphml")
nx.write_graphml(cd_controlado, "cd_controlado.graphml")
nx.write_graphml(cd_controlado_esteiras, "cd_controlado_esteiras.graphml")

print("Centro de Distribuições salvos")"""

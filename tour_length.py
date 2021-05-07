import math
from itertools import permutations
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import networkx as nx
from networkx.algorithms import tree
from networkx.utils import UnionFind
from random import choice
import numpy as np

def tour_length(P):
    'returns length of tour P'
    dist = 0
    for i in range(len(P)-1):
        x1 = P[i][0]
        y1 = P[i][1]
        x2 = P[i+1][0]
        y2 = P[i+1][1]
        dist+= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    x1 = P[-1][0]
    y1 = P[-1][1]
    x2 = P[0][0]
    y2 = P[0][1]
    dist+= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    return (dist)

def distance(x1,y1,x2,y2):
    'returns distance of two points'
    dist = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    return dist
        
def TSP(P):
    'traveling salesman implementation'
    tour_min = tour_length(P)
    final_perm = []
    for perm in permutations(P):
        if tour_length(perm) < tour_min:
            tour_min = tour_length(perm)
            final_perm = perm
    print(tour_min)
    return list(final_perm)

def build_graph(P):
    'builds a graph out of P'
    G = nx.Graph()
    for i in range(len(P)):
        for j in range(len(P)):
            if j != i:
                G.add_edge(i,j, weight = distance(P[i][0],P[i][1],P[j][0],P[j][1]))
    
    #elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    #esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
    #pos = nx.spring_layout(G)  # positions for all nodes
    # nodes
    #nx.draw_networkx_nodes(G, pos, node_size=700)
    # edges
    #nx.draw_networkx_edges(G, pos, edgelist=elarge, width=1)
    #nx.draw_networkx_edges(
    #    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    #)
    # labels
    #nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    #plt.axis("off")
    #plt.show()
    return G
       
        
def approx_TSP(P):
    'returns approx best tour of P'
    G = build_graph(P)
    
    mst = tree.minimum_spanning_edges(G, algorithm='kruskal',data=False)
    edgelist = list(mst)
   
    T = nx.Graph()
    T.add_edges_from(edgelist)

    lst = list(nx.dfs_preorder_nodes(T))
    newLst = []
    for i in lst:
        newLst.append(P[i])
    #print(tour_length(newLst))
    return newLst

def cities(k,n):
    'create k cities in nxn grid'

    city_set = set()
    while len(city_set) < k:
        city_set.add((choice(range(n)),choice(range(n))))
    return list(city_set)



def visual_TSP(P):
    'draws both the optimal solution and the approx graph'
    vertices1 = TSP(P)
    vertices1.append(vertices1[0])
    x1 = []
    y1 = []
    for i in vertices1:
        x1.append(i[0])
        y1.append(i[1])
    plt.plot(x1,y1,label = "TPS",linewidth=5)

    vertices2 = approx_TSP(P)
    vertices2.append(vertices2[0])
    x2 = []
    y2 = []
    for i in vertices2:
        x2.append(i[0])
        y2.append(i[1])
    plt.plot(x2,y2,label = "approx_TPS",linewidth = 2)
    plt.legend()
    plt.show()
    
        
    
    
   
    

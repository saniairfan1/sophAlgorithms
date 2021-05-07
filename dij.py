import networkx as nx

def G():
    G = nx.DiGraph()
    G.add_weighted_edges_from([('s','a',0),('s','b',-1),('a','b',-2)])
    print(nx.bellman_ford_path(G,'s','b'))
    

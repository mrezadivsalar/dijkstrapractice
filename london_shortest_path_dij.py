# finding shortest distance between two underground station london with built-in dijkstra in netwrokx lib

# Read London underground data.
import networkx as nx
import pandas as pd
tube_data = pd.read_excel('tube_data.xls', sheet_name='Runtime')
tube_data.describe()

G = nx.Graph()
for index, item in tube_data.iterrows():
    G.add_edge(item['Station from (A)'], item['Station to (B)'], weight=item['AM peak (0700-1000) Running Time (Mins)'])

# Get all edges with weights 
all_edges = G.edges(data=True)

all_shortest_dists = nx.all_pairs_dijkstra_path_length(G)
all_shortest_paths = nx.all_pairs_dijkstra_path(G)

all_shortest_dists_dict = dict(all_shortest_dists)
all_shortest_paths_dict = dict(all_shortest_paths)

all_shortest_dists_dict['SOUTH KENSINGTON']['LIVERPOOL STREET']
all_shortest_paths_dict['SOUTH KENSINGTON']['LIVERPOOL STREET']
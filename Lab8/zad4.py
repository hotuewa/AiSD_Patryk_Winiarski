import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E"),
    ("E", "F"),
    ("F", "A")
])

pos = nx.spring_layout(G, seed=12)  

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=14, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{u}-{v}" for u, v in G.edges()}, font_color='red')

plt.title("Graf nieskierowany z 6+ wierzchołkami", fontsize=16)
plt.axis('off')
plt.show()
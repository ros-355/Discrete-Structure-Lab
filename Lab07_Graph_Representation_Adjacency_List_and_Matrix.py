"""
LAB 07: Graph Representation using Adjacency List and Adjacency Matrix

Required libraries:
- networkx
- matplotlib

Install if needed:
    pip install networkx matplotlib

Theory:
A graph G=(V,E) contains vertices V and edges E.

Adjacency list:
For each vertex, store its neighbouring vertices.

Adjacency matrix:
A matrix M where M[i][j] = 1 if there is an edge between vertex i and j.

Aim:
1. Represent a graph with an adjacency list.
2. Build its adjacency matrix.
3. Draw the graph using NetworkX.

Conclusion:
Adjacency lists are memory-efficient for sparse graphs, while adjacency
matrices make edge checking very direct.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx


vertices = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D")
]

# Adjacency list
adj_list = {v: [] for v in vertices}

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

print("Adjacency List:")
for v in vertices:
    print(v, "->", adj_list[v])

# Adjacency matrix
matrix = []
for u in vertices:
    row = []
    for v in vertices:
        row.append(1 if v in adj_list[u] else 0)
    matrix.append(row)

print("\nAdjacency Matrix:")
print("   ", *vertices)
for v, row in zip(vertices, matrix):
    print(v, " ", *row)

# Draw graph
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)

plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G, seed=7)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1800,
    font_size=12
)
plt.title("Graph Representation")
output_file = "Lab07_Graph.png"
plt.savefig(output_file, bbox_inches="tight")
plt.close()

print(f"\nGraph image saved as: {output_file}")

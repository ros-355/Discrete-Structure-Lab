"""
LAB 03: Relation Properties, Matrix, and Digraph Representation

Required libraries:
- networkx
- matplotlib

Install if needed:
    pip install networkx matplotlib

Theory:
A relation R on a set A is a set of ordered pairs.

Important properties:
Reflexive   : (a,a) belongs to R for every a in A
Symmetric   : if (a,b) is in R, then (b,a) is also in R
Antisymmetric: if (a,b) and (b,a) are both in R, then a=b
Transitive  : if (a,b) and (b,c) are in R, then (a,c) is in R

Aim:
1. Test common properties of a relation.
2. Create the relation matrix.
3. Draw the relation as a directed graph.

Conclusion:
The program checks relation properties and represents the same relation using
both a matrix and a directed graph.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx


A = {1, 2, 3}
R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)}


def is_reflexive(A, R):
    return all((a, a) in R for a in A)


def is_symmetric(R):
    return all((b, a) in R for (a, b) in R)


def is_antisymmetric(R):
    return all(a == b or (b, a) not in R for (a, b) in R)


def is_transitive(R):
    for a, b in R:
        for x, c in R:
            if b == x and (a, c) not in R:
                return False
    return True


print("Set A =", A)
print("Relation R =", sorted(R))
print("Reflexive:", is_reflexive(A, R))
print("Symmetric:", is_symmetric(R))
print("Antisymmetric:", is_antisymmetric(R))
print("Transitive:", is_transitive(R))

# Relation matrix
elements = sorted(A)
matrix = [[1 if (i, j) in R else 0 for j in elements] for i in elements]

print("\nRelation Matrix")
print("   ", *elements)
for e, row in zip(elements, matrix):
    print(e, " ", *row)

# Digraph
G = nx.DiGraph()
G.add_nodes_from(elements)
G.add_edges_from(R)

plt.figure(figsize=(6, 5))
pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1800,
    arrowsize=20,
    font_size=12
)
plt.title("Digraph of Relation R")
output_file = "Lab03_Relation_Digraph.png"
plt.savefig(output_file, bbox_inches="tight")
plt.close()

print(f"\nDigraph saved as: {output_file}")

"""Python Code 8: Finding a Spanning Tree."""

import networkx as nx
import matplotlib.pyplot as plt


# Create a connected undirected graph.
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3),
                  (2, 4), (3, 5), (4, 5)])

# Find one spanning tree.
T = nx.minimum_spanning_tree(G)

print("Edges of the original graph:", list(G.edges))
print("Edges of the spanning tree:", list(T.edges))
print("Number of tree edges:", T.number_of_edges())

# A spanning tree of n nodes has n-1 edges.
print("n - 1 =", T.number_of_nodes() - 1)

# Draw the original graph and the tree.
position = nx.spring_layout(G, seed=3)

plt.subplot(1, 2, 1)
nx.draw(G, position, with_labels=True, node_color="lightgray")
plt.title("Original graph")

plt.subplot(1, 2, 2)
nx.draw(T, position, with_labels=True, node_color="lightblue")
plt.title("Spanning tree")

plt.tight_layout()
plt.show()

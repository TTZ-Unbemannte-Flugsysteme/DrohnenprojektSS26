"""Python Code 9: Root of a Directed Spanning Tree."""

import networkx as nx
import matplotlib.pyplot as plt


# Information flows in the direction of each arrow.
G = nx.DiGraph()
G.add_edges_from([(2, 1), (2, 3), (3, 4),
                  (4, 5), (2, 6)])

# A root can reach every other node.
roots = []

for node in G.nodes:
    reachable = nx.descendants(G, node)

    if len(reachable) == G.number_of_nodes() - 1:
        roots.append(node)

print("Possible roots:", roots)

# Draw the graph.
position = nx.spring_layout(G, seed=5)
colors = []

for node in G.nodes:
    if node in roots:
        colors.append("orange")
    else:
        colors.append("lightblue")

nx.draw(G, position, with_labels=True, node_color=colors,
        node_size=900, arrowsize=20)
plt.title("Orange node = root of a directed spanning tree")
plt.show()

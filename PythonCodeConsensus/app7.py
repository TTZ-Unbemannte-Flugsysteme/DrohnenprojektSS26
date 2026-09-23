"""Python Code 7: Connected Components."""

import networkx as nx
import matplotlib.pyplot as plt


# Create an undirected graph with two separate groups.
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 5), (5, 6)])

# Find the connected components.
components = list(nx.connected_components(G))

print("Number of connected components:", len(components))
print("Components:", components)

# Draw the disconnected graph.
position = nx.spring_layout(G, seed=1)
nx.draw(G, position, with_labels=True, node_size=900,
        node_color="lightgreen")
plt.title("A graph with two connected components")
plt.show()

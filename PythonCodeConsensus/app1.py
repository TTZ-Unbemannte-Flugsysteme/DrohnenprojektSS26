"""Python Code 1: Representing a Graph."""

import networkx as nx
import matplotlib.pyplot as plt


# Create an empty directed graph.
G = nx.DiGraph()

# Add six agents.
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# An edge (j, i) means that agent j sends information to agent i.
edges = [(2, 1), (1, 4), (2, 4), (4, 3),
         (3, 2), (2, 6), (6, 5), (5, 2)]
G.add_edges_from(edges)

# Print the graph data.
print("Agents:", list(G.nodes))
print("Connections:", list(G.edges))

# Draw the graph.
position = nx.circular_layout(G)
nx.draw(G, position, with_labels=True, node_size=900,
        node_color="lightblue", arrowsize=20)
plt.title("Directed communication graph")
plt.show()

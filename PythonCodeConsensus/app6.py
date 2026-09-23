"""Python Code 6: Paths and Connectivity."""

import networkx as nx


# Create a directed graph.
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 5)])

# Check whether a path exists from agent 1 to agent 5.
if nx.has_path(G, 1, 5):
    path = nx.shortest_path(G, 1, 5)
    print("A path from 1 to 5 is:", path)
else:
    print("There is no path from 1 to 5.")

# Strong connectivity requires a directed path in both directions.
print("Strongly connected:", nx.is_strongly_connected(G))

# Weak connectivity ignores the arrow directions.
print("Weakly connected:", nx.is_weakly_connected(G))

"""Python Code 2: Neighbors and Degrees."""

import networkx as nx


# Create the directed graph.
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5, 6])
G.add_edges_from([(2, 1), (1, 4), (2, 4), (4, 3),
                  (3, 2), (2, 6), (6, 5), (5, 2)])

# Inspect one agent at a time.
for i in G.nodes:
    in_neighbors = list(G.predecessors(i))
    out_neighbors = list(G.successors(i))

    print("Agent", i)
    print("  In-neighbors :", in_neighbors)
    print("  Out-neighbors:", out_neighbors)
    print("  In-degree    :", G.in_degree(i))
    print("  Out-degree   :", G.out_degree(i))

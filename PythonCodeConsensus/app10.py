"""Python Code 10: Testing Whether a Directed Graph Is Balanced."""

import networkx as nx


# A directed cycle is balanced.
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

balanced = True

for i in G.nodes:
    in_degree = G.in_degree(i)
    out_degree = G.out_degree(i)

    print("Agent", i, ": in-degree =", in_degree,
          ", out-degree =", out_degree)

    if in_degree != out_degree:
        balanced = False

print("\nIs the graph balanced?", balanced)

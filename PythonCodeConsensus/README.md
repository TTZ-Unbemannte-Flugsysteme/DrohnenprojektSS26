# Multi-Agent Systems: Simple Python Codes 1-25

This package is written for a line-by-line classroom explanation. Each file is
standalone, uses short loops, and demonstrates only one main idea. The examples
avoid classes, compact programming tricks, and hidden helper modules.

## Installation

```bash
python -m pip install -r requirements.txt
```

Run one example at a time:

```bash
python app1.py
python app11.py
python app25.py
```

## Code sequence

| File | Classroom title |
|---:|---|
| `app1.py` | Representing a directed graph |
| `app2.py` | Neighbors and in/out-degrees |
| `app3.py` | Adjacency matrix and edge direction |
| `app4.py` | Degree and Laplacian matrices |
| `app5.py` | Laplacian properties and eigenvalues |
| `app6.py` | Paths and connectivity |
| `app7.py` | Connected components |
| `app8.py` | Finding a spanning tree |
| `app9.py` | Root of a directed spanning tree |
| `app10.py` | Testing graph balance |
| `app11.py` | Continuous-time consensus in the book style |
| `app12.py` | Continuous average consensus |
| `app13.py` | Continuous consensus on a balanced digraph |
| `app14.py` | Continuous consensus on an unbalanced digraph |
| `app15.py` | Failure without a spanning tree |
| `app16.py` | Basic discrete-time consensus loop |
| `app17.py` | Perron matrix and average consensus |
| `app18.py` | Safe and unsafe step sizes |
| `app19.py` | Discrete consensus on a balanced digraph |
| `app20.py` | Discrete consensus on an unbalanced digraph |
| `app21.py` | Measuring the consensus error |
| `app22.py` | Leader-follower consensus |
| `app23.py` | Consensus of two-dimensional positions |
| `app24.py` | Consensus with switching graphs |
| `app25.py` | Continuous versus discrete consensus |

## Important convention

In the consensus equations, `N[i]` is the list of agents that send information
to agent `i`. Therefore, if `j` is in `N[i]`, the local difference used by
agent `i` is:

```python
x[j] - x[i]
```

Some scripts insert an unused agent `0`. This makes the Python indices equal to
the labels in the graph: agents `1, 2, ..., N`.

Primary reference: M. Nagahara, S.-I. Azuma, and H.-S. Ahn, *Control of
Multi-agent Systems: Theory and Simulations with Python*, Springer, 2024.

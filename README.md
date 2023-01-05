# Adjacency-Matrix

This repository contains a collection of Python implementations for working with adjacency matrices. An adjacency matrix is a square matrix that represents a finite graph, with rows and columns corresponding to vertices, and the presence of an edge between two vertices indicated by a non-zero value in the matrix. Adjacency matrices are a useful representation of graphs because they allow for efficient operations such as determining the degree of a vertex, finding the neighbors of a vertex, and traversing the graph.

### Implementations

**Adjacency Matrix**: A basic implementation of an adjacency matrix class that supports adding and removing edges, determining the degree of a vertex, and finding the neighbors of a vertex.

**Weighted Adjacency Matrix**: An extension of the adjacency matrix class that supports weighted edges, with the weight of an edge represented by a non-zero value in the matrix.

**Sparse Adjacency Matrix**: An implementation of an adjacency matrix using a sparse matrix representation, which is more memory-efficient for graphs with a large number of vertices and a small number of edges.

### Example
```python
# Create an adjacency matrix with 5 vertices
matrix = AdjacencyMatrix(5)

# Add edges to the matrix
matrix.add_edge(0, 1)
matrix.add_edge(0, 2)
matrix.add_edge(1, 2)
matrix.add_edge(2, 3)
matrix.add_edge(3, 4)

# Print the matrix
print(matrix)

# Output:
# [[0 1 1 0 0]
#  [1 0 1 0 0]
#  [1 1 0 1 0]
#  [0 0 1 0 1]
#  [0 0 0 1 0]]

# Determine the degree of vertex 0
degree = matrix.degree(0)
print(f"Vertex 0 has degree {degree}")

# Output: Vertex 0 has degree 2

# Find the neighbors of vertex 0
neighbors = matrix.neighbors(0)
print(f"Vertex 0 has neighbors {neighbors}")

# Output: Vertex 0 has neighbors [1, 2]
```
Question:
Display a sub-tree at a given vertex of a given rooted tree, when the graph is represented using an adjacency matrix. Also compute the height of the trees.

If you have any suggestions or improvements for the implementations in this repository, feel free to create a pull request or open an issue. Contributions are welcome!

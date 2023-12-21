# SciPy Graphs

# Working with Graphs
  # Graphs are an essential data structure.
  # SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

# Adjacency Matrix
   # Adjacency matrix is a nxn matrix where n is the number of elements in a graph.
   # And the values represents the connection between the elements.

# Example:

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csc_matrix

arr = np.array([[0, 1, 2],[1, 0, 0],[2, 0, 0]])

newarr = csc_matrix(arr)
print(connected_components(newarr))

# Dijkstra
   # Use the dijkstra method to find the shortest path in a graph from one element to another.
   # It takes following arguments:
      # return_predecessors: boolean (True to return whole path of traversal otherwise False).
      # indices: index of the element to return all paths from that element only.
      # limit: max weight of path.
# Example
   # Find the shortest path from element 1 to 2:

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csc_matrix

arr = np.array([[0, 1, 2],[1, 0, 0],[2, 0, 0]])
newarr = csc_matrix(arr)

print(dijkstra(newarr, return_predecessors = True, indices = 0))

# Floyd Warshall
   # Use the floyd_warshall() method to find shortest path between all pairs of elements.

# Example
   # Find the shortest path between all pairs of elements:

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([[0, 1, 2],[1, 0, 0],[2, 0, 0]])
newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors = True))


# Bellman Ford
  # The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.

# Example
  # Find shortest path from element 1 to 2 with given graph with a negative weight:

import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([[0, -1, 2],[1, 0, 0],[2, 0, 0]])
newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors = True, indices = 0))


# Depth First Order
   # The depth_first_order() method returns a depth first traversal from a node.
   # This function takes following arguments:
      # the graph.
      # the starting element to traverse graph from.
# Example
   # Traverse the graph depth first for given adjacency matrix:

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([[0, 1, 0, 1],[1, 1, 1, 1],[2, 1, 1, 0],[0, 1, 0, 1]])

newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

# Breadth First Order
  # The breadth_first_order() method returns a breadth first traversal from a node.
  # This function takes following arguments:
      # the graph.
      # the starting element to traverse graph from.
# Example
    # Traverse the graph breadth first for given adjacency matrix:

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([[0, 1, 0, 1],[1, 1, 1, 1],[2, 1, 1, 0],[0, 1, 0, 1]])

newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))


# Own notes: # Connected_components - In the super graph, there are number of subgraphs - One component contains the number of connected nodes,  Not connected node is considered as seperate component. 
             # dijkstra  - To find the shortest path in a graph from one element to another that includes the following arguement - (return_predecessors = True, indices = 0)
             # floyd_warshall - To find the shortest part between all pairs of elements  that include only 'return_predecessors=True.
             # bellman_ford - This method also to find the shortest part between all pairs of elements same as floyd_warshall but it can handle the negative weight as well. Properties need to add in this similiar to Dijkstra. 
             # Depth first order-  only need to put 1 after newarr while print it. 
             # Breadth first order - only need to put 1 after newarr while print it.

            # Explanation:
# Connected Components : In the super graph, there are number of subgraphs - One component contains the number of connected nodes,  Not connected node is considered as seperate component. 
# Dijkstra algoritham : Used to FIND THE SHORTEST PATH (WITH MINIMAL COST) TO REACH FROM ONE NODE TO ANOTHER (it's may be direct reach or via in between nodes, cost has to be added to find out the final minimal cost)
# Floyd_Warshall algoritham: Used TO FIND THE SHORTEST PATH BETWEEN ALL THE PAIRS OF VERITICES IN A WEIGHTED GRAPH. This algorithm works for both the directed and undirected weighted graphs. (ONLY POSITIVE WEIGHTS)
# Bellman ford : SAME AS FLOYD_WARSHALL BUT IT CAN HANDLE (DETECTS) THE NEGATIVE WEIGHTS CYCLE AS WELL

# What is the difference between Bellman-Ford and Floyd-Warshall algorithm?
    # The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph whereas Floyd-Warshall computes shortest paths from each node to every other node.

# Floyd Warshall works for negative edge but no negative cycle, whereas Dijkstra's algorithm don't work for negative edges.
# Dijkstra's algorithm is better when it comes to reducing the time complexity.
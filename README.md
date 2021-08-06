# DFS to find fathers of SINKs vertices

This DFS generate a list of lists of father of SINKs vertices, and also downward of a initial vertex.

### Example:
  - Vertex 1 is SINK and downward of initial vertex, and fathers of vertex 1 is 5 and 6;
  - Vertex 2 isn't SINK but is downward of initial vertex and one of it fathers is 7;
  - Vertex 3 isn't downward of initial vertex.
  
  __Return of dfs__: [[5,6], [7], []]  
                    1     2    3

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

The program also print the vertices that the distance (d[X]+d[Y]) are the minium, when X and Y are the fathers of a SINK vertex.
Moreover, I used a Graph class and a function to read a pajek file

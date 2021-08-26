# DFS to find fathers of SINKs vertices

This DFS generate a list of lists of father of SINKs vertices, and also descendant of a initial vertex.  
OBS.: the DFS code starts at line 64  

### Example:
  - Vertex 5 is SINK and descendant of initial vertex, and fathers of vertex 1 is 1 and 2;
  - Vertex 6 isn't SINK but is descendant of initial vertex and one of it fathers is 3;
  - Vertex 7 ave only one father descendant of initial vertex and it is 4.
  - Vertex 8 isn't descendant of initial vertex
  
  __Return of dfs__: 
<pre>
                 [[], [], [], [], [1,2], [3], [4], []] 
                  1   2   3   4     5     6    7   8
</pre>

### Additional:

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.

The program also print the vertices that the distance (d[X]+d[Y]) are the minium, when X and Y are the fathers of a SINK vertex descendant of the initial vertex 1.  

Moreover, I used a Graph class and a function to read a pajek file.

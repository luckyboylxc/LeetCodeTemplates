# A Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# The main function that finds shortest distances
# from src to all other vertices using Bellman-
# Ford algorithm. The function also detects
# negative weight cycle
def isNegCycleBellmanFord(src, dist):
    global graph, V, E

    # Step 1: Initialize distances from src
    # to all other vertices as INFINITE
    for i in range(V):
        dist[i] = 10**18
    dist[src] = 0

    # Step 2: Relax all edges |V| - 1 times.
    # A simple shortest path from src to any
    # other vertex can have at-most |V| - 1
    # edges
    for i in range(1,V):
        for j in range(E):
            u = graph[j][0]
            v = graph[j][1]
            weight = graph[j][2]
            if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
                dist[v] = dist[u] + weight

    # Step 3: check for negative-weight cycles.
    # The above step guarantees shortest distances
    # if graph doesn't contain negative weight cycle.
    # If we get a shorter path, then there
    # is a cycle.
    for i in range(E):
        u = graph[i][0]
        v = graph[i][1]
        weight = graph[i][2]
        if (dist[u] != 10**18 and dist[u] + weight < dist[v]):
            return True

    return False
# Returns true if given graph has negative weight
# cycle.
def isNegCycleDisconnected():
    global V, E, graph
    
    # To keep track of visited vertices to avoid
    # recomputations.
    visited = [0]*V
    # memset(visited, 0, sizeof(visited))

    # This array is filled by Bellman-Ford
    dist = [0]*V

    # Call Bellman-Ford for all those vertices
    # that are not visited
    for i in range(V):
        if (visited[i] == 0):
            
            # If cycle found
            if (isNegCycleBellmanFord(i, dist)):
                return True

            # Mark all vertices that are visited
            # in above call.
            for i in range(V):
                if (dist[i] != 10**18):
                    visited[i] = True
    return False

# Driver code
if __name__ == '__main__':
    
    # /* Let us create the graph given in above example */
    V = 5 # Number of vertices in graph
    E = 8 # Number of edges in graph
    graph = [[0, 0, 0] for i in range(8)]

    # add edge 0-1 (or A-B in above figure)
    graph[0][0] = 0
    graph[0][1] = 1
    graph[0][2] = -1

    # add edge 0-2 (or A-C in above figure)
    graph[1][0] = 0
    graph[1][1] = 2
    graph[1][2] = 4

    # add edge 1-2 (or B-C in above figure)
    graph[2][0] = 1
    graph[2][1] = 2
    graph[2][2] = 3

    # add edge 1-3 (or B-D in above figure)
    graph[3][0] = 1
    graph[3][1] = 3
    graph[3][2] = 2

    # add edge 1-4 (or A-E in above figure)
    graph[4][0] = 1
    graph[4][1] = 4
    graph[4][2] = 2

    # add edge 3-2 (or D-C in above figure)
    graph[5][0] = 3
    graph[5][1] = 2
    graph[5][2] = 5

    # add edge 3-1 (or D-B in above figure)
    graph[6][0] = 3
    graph[6][1] = 1
    graph[6][2] = 1

    # add edge 4-3 (or E-D in above figure)
    graph[7][0] = 4
    graph[7][1] = 3
    graph[7][2] = -3

    if (isNegCycleDisconnected()):
        print("Yes")
    else:
        print("No")

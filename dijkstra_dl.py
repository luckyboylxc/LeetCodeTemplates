import heapq

def dijkstra(graph,n,source):
    visited = [False] * n
    distance = [float('inf')] *n
    distance[source] = 0
    pq = []
    pq.append((0,source))
    while(pq):
        currDistance,currNode = heapq.heappop(pq)
        if(currNode in visited):
            continue

        visited[currNode] = True
        
        for u,cost in graph[currNode]:
            if(visited[u]):
                continue
            if(currDistance+cost<distance[u]):
                distance[u] = currDistance+cost
                heapq.heappush(pq,(distance[u],u))
    
    return distance
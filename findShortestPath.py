def shortest_path(V, edges, start, end):
   
    if start == end:
        return 0
   
    graph = {}
    for i in range(V):
        graph[i] = []
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    
    queue = [(start, 0)]  
    visited = [False] * V  
    visited[start] = True
    
    while queue:
        node, distance = queue.pop(0) 
        
      
        for neighbor in graph[node]:
            if neighbor == end:
                return distance + 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    
   
    return -1


print(shortest_path(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0, 4)) 
print(shortest_path(3, [[0, 1], [1, 2]], 0, 2))
print(shortest_path(4, [[0, 1], [1, 2]], 2, 3)) 
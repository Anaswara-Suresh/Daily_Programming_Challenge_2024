def hasCycle(V,edges):
   
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
 
    visited=[False]*V

    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):  
                    return True
            elif neighbor!=parent:  
                return True
        return False
    
   
    for i in range(V):
        if not visited[i]:  
            if dfs(i,-1):  
                return True
    
    return False


if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))
    
    edges = []
    print(f"Enter the {E} edges (as pairs of space-separated integers):")
    for _ in range(E):
        u,v=map(int,input().split())
        edges.append([u,v])
    
    
    if hasCycle(V,edges):
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")

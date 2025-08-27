class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
       # print(adj)
        visited = set()
        
        def dfs(n):
            
            if n in visited:
                return
        
            visited.add(n)
            for nei in adj[n]:
                if nei not in visited:
                    
                    dfs(nei)      
        c = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                c +=1
        return c

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # barti
        n = len(edges)
        
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, node):
                        return True
                elif nei != parent:
                    return True
            return False
        
        for u, v in reversed(edges):
     
            adj[u].remove(v)
            adj[v].remove(u)
            
            visited.clear()
            has_cycle = False
            for i in range(1, n+1):
                if i not in visited:
                    if dfs(i, -1):
                        has_cycle = True
                        break
        
            if not has_cycle:
                return [u, v]
        
            adj[u].append(v)
            adj[v].append(u)


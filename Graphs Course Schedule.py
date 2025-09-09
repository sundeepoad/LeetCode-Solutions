class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #barti

        hp = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            hp[crs].append(pre)
        

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if hp[crs] == []:
                return True
            
            visited.add(crs)
            for pre in hp[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            hp[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

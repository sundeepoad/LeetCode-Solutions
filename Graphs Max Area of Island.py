class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])

        islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
        
            area = 1
            grid[r][c]= 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
               # area += 1
            
           # maxarea = max(maxarea,area)

        maxarea = 0
        for r in range(rows):
            for c in range(cols):
              if grid[r][c] == 1:
            
    
                maxarea = max(maxarea, dfs(r,c))
        return maxarea
        

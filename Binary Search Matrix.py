class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(matrix,target):

            left = 0
            right = len(matrix) - 1

           # print(left, right)

            while left <= right:
                mid = (left + right) // 2

                if matrix[mid] > target:
                    right = mid - 1
                    
            
                elif matrix[mid] < target:
                    left = mid + 1
                    
            
                elif matrix[mid] == target:
                    return True
        
            return False
        
  
        for i in range(len(matrix)):
            last = (matrix[i][-1])
            first = (matrix[i][0])

            if target >= first and target <= last:
                rest = (binary(matrix[i],target))
                return rest
            else:
                continue
        return False

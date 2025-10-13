class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = []
        for i in stones:
            lst.append(-i)

        #print(lst)   
        self.heap = lst
        heapq.heapify(self.heap)
        
        while len(self.heap) > 1:
            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)

            if y > x:
                heapq.heappush(self.heap, x - y)
            
     
        self.heap.append(0)
        return abs(self.heap[0])
        #print("heap:",self.heap)
        


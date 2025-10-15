class MedianFinder:

    def __init__(self):

        self.lst = []
        

    def addNum(self, num: int) -> None:

        self.lst.append(num)
        

    def findMedian(self) -> float:
        self.lst.sort()
        l = len(self.lst)
        print("length: ", l)

        
        if l == 1:
            return self.lst[0]
        
        if l % 2 == 0:
            mid = l // 2
            p = ((self.lst[mid] + self.lst[mid-1]) / 2)
            return (p)
        
        if l % 2 != 0:
            mid1 = l // 2
            return self.lst[mid1]

        
        

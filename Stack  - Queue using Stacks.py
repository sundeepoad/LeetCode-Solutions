class MyQueue:

    def __init__(self):
        self.queue = []        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.queue = self.queue[::-1]
        m = self.queue.pop()
        self.queue = self.queue[::-1]
    
        return m
      #  return p

    def peek(self) -> int:
        q = self.queue[0]
        return q

    def empty(self) -> bool:
        
        if len(self.queue) == 0:
            return True
        else:
            return False

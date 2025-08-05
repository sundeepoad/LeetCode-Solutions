class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        stack = []
        for i in logs:
            if i == "../" and stack:
                stack.pop()
            
            elif i == "./":
                continue
            
            elif i != "../" and i != "./":
                stack.append(i)
        print(stack)
        return (len(stack))


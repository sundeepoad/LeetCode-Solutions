class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## barti

       # stack = []
        final = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ind = stack.pop()
                final[ind] = i - ind
            stack.append(i)
        return final



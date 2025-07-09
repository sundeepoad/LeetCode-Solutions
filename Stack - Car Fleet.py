class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # barti

        pair = sorted(zip(position,speed), reverse = True)
        #print(pair)
        stack = []
        for p, s in pair:
            time = (target - p) / s

            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

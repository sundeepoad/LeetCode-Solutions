class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        curr = []
        if not digits:
            return []
        hm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            
            for j in hm[digits[i]]:
                curr.append(j)
                dfs(i+1)
                curr.pop()
        
        dfs(0)
        return res

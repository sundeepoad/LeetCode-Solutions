class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## do again
        d = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):

            d[s[r]] += 1
            maxi = max(d.values())
            curr = r - l + 1

            if curr - maxi > k:
                d[s[l]] -= 1
                l +=1
            
            res = max(res, r - l + 1)
        return res

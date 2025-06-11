class Solution:

    def encode(self, strs: List[str]) -> str:
            ## barti
        lst = ""

        for i in strs:
            lst += str(len(i)) + '#' + i
        return lst

    def decode(self, s: str) -> List[str]:

        lst = []
        p = 0

        while p < len(s):
            q = p

            while s[q] != '#':
                q+=1
            length = int(s[p:q])
            p = q + 1
            q = p + length

            lst.append(s[p:q])
            p = q
        return lst


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:


        if (len(word1) != len(word2)) or (set(word1) != set(word2)):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        p = sorted(freq1.values())
        q = sorted(freq2.values())

        if p != q:
            return False
        return True
        

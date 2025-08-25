

class WordDictionary:

    def __init__(self):

        self.lst = []

    def addWord(self, word: str) -> None:

        self.lst.append(word)
        

    def search(self, word: str) -> bool:

        for w in self.lst:
            if len(w) != len(word):
                continue
            
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == ".":
                    i+=1
                
                else:
                    break
            if i == len(w):
                return True
        return False

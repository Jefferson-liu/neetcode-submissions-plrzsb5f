
class PrefixTree:

    def __init__(self):
        self.head = {}


    def insert(self, word: str) -> None:
        
        curDict = self.head
        for letter in word:
            if letter not in curDict:
                curDict[letter] = {}
            curDict = curDict[letter]
        curDict["."] = True
 


    def search(self, word: str) -> bool:
        curDict = self.head
        for letter in word:
            if letter not in curDict:
                return False
            curDict = curDict[letter]
        if "." not in curDict:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curDict = self.head
        for letter in prefix:
            if letter not in curDict:
                return False
            curDict = curDict[letter]
        return True
        
        
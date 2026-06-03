class PrefixTree:

    def __init__(self):
        self.wordList = []

    def insert(self, word: str) -> None:
        if word not in self.wordList:
            self.wordList.append(word)

    def search(self, word: str) -> bool:
        return word in self.wordList

    def startsWith(self, prefix: str) -> bool:
        for word in self.wordList:
            if word[:len(prefix)] == prefix:
                return True
        return False
        
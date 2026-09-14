class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.rootNode = TrieNode()

    def addWord(self, word: str) -> None:
        curNode = self.rootNode
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = TrieNode()
            curNode = curNode.children[letter]
        curNode.end = True

    def search(self, word: str) -> bool:
        curNode = self.rootNode
        return self.dfs(word, curNode)
    
    def dfs(self, word, root):
        if len(word) == 0:
            if root.end == True:
                return True
            return False
        if word[0] != '.':
            if word[0] not in root.children:
                return False
            else:
                return self.dfs(word[1:], root.children[word[0]])
        else:
            for child in root.children:
                if self.dfs(word[1:], root.children[child]):
                    return True
        return False
            
            
        

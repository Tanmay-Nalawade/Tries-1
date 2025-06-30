class Trie:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if  curr.children[idx] == None:
                curr.children[idx] = self.TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True
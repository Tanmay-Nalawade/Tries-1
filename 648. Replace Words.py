class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_end = False
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []
        self.root = self.TrieNode()
        for word in dictionary:
            curr = self.root
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] == None:
                    curr.children[idx] = self.TrieNode()
                curr = curr.children[idx]
            curr.is_end = True


        for word in sentence.split():
            curr = self.root
            prefix = ""
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] == None or curr.is_end == True:
                    break
                prefix += char
                curr = curr.children[idx]
            if curr.is_end:
                result.append(prefix)
            else:
                result.append(word)

        return ' '.join(result)
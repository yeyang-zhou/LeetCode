class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        def match(node, idx):
            if idx == len(word):
                return '#' in node
            ch = word[idx]
            if ch == '.':
                for k, v in node.items():
                    if k == '#':
                        continue
                    if match(v, idx+1):
                        return True
                return False
            if ch not in node:
                return False
            return match(node[ch], idx+1)
        return match(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

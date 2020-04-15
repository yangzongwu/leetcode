class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p=self.dicts
        for s in word:
            if s not in p:
                p[s]={}
                p=p[s]
            else:
                p=p[s]
        p['#']=None
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p=self.dicts
        for s in word:
            if s not in p:
                return False
            else:
                p=p[s]
        return '#' in p
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p=self.dicts
        for s in prefix:
            if s not in p:
                return False
            else:
                p=p[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

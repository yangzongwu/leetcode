class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts={}

    def insert(self, word: 'str') -> 'None':
        """
        Inserts a word into the trie.
        """
        p=self.dicts
        for c in word:
            if c not in p:
                p[c]={}
            p=p[c]
        p['#']=True
        

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the trie.
        """
        if self.find(word) and '#' in self.find(word):
            return True
        return False

    def startsWith(self, prefix: 'str') -> 'bool':
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if self.find(prefix):
            return True
        return False
        
        
    def find(self,prefix):
        p=self.dicts
        for c in prefix:
            if c not in p:
                return None
            else:
                p=p[c]
        return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

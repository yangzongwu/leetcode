'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts={}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p=self.dicts
        for c in word:
            if c not in p:
                p[c]={}
            p=p[c]
        p['#']=True
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node=self.find(word)
        if node is not None and '#' in node:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node=self.find(prefix)
        if node is not None:
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

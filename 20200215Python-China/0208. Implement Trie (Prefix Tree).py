### [208\. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

Difficulty: **Medium**


Implement a trie with `insert`, `search`, and `startsWith` methods.

**Example:**

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

**Note:**

*   You may assume that all inputs are consist of lowercase letters `a-z`.
*   All inputs are guaranteed to be non-empty strings.


#### Solution

Language: **Python3**

```python3
    def __init__(self,val):
        self.val=val
        self.children=[]
    
class Trie:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie=TreeNode('_')
​
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        word+='#'
        node=self.trie
        for w in word:
            flag=False
            for child in node.children:
                if child.val==w:
                    node=child
                    flag=True
                    break
            if flag==False:
                newnode=TreeNode(w)
                node.children.append(newnode)
                node=newnode
        
        
​
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        word+='#'
        node=self.trie
        for w in word:
            flag=False
            for child in node.children:
                if child.val==w:
                    flag=True
                    node=child
                    break
            if flag==False:
                return False
        return True
​
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.trie
        for w in prefix:
            flag=False
            for child in node.children:
                if child.val==w:
                    flag=True
                    node=child
                    break
            if flag==False:
                return False
        return True
​
​
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

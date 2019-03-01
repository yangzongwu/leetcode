class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictword={}

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        p=self.dictword
        for s in word:
            if s not in p:
                p[s]={}
                p=p[s]
            else:
                p=p[s]
        p['#']=None
    
    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        def dfs(word,dictword):
            if not word: 
                if '#' in dictword:
                    return True
                else:
                    return False
            for k in range(len(word)):
                if word[k]!='.':
                    if word[k] not in dictword:
                        return False
                    else:
                        return dfs(word[k+1:],dictword[word[k]])
                else:
                    for ss in 'qwertyuiopasdfghjklzxcvbnm':
                        if ss in dictword and dfs(word[k+1:],dictword[ss]):
                            return True
                    return False
        return dfs(word,self.dictword)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

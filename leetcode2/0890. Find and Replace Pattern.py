class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        rep=[]
        for word in words:
            if len(word)==len(pattern):
                if self.subfindAndReplacePattern(word,pattern):
                    rep.append(word)
        return rep
    
    def subfindAndReplacePattern(self,word,pattern):
        dictword={}
        usedword=set()
        for k in range(len(word)):
            if word[k] not in dictword:
                if pattern[k] not in usedword:
                    dictword[word[k]]=pattern[k]
                    usedword.add(pattern[k])
                else:
                    return False
            else:
                if pattern[k]!=dictword[word[k]]:
                    return False
        return True

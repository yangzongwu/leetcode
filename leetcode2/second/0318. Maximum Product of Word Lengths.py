class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        wordset=[]
        
        for word in words:
            cur=set()
            for s in word:
                cur.add(s)
            wordset.append(cur)
        
        rep=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(wordset[i])+len(wordset[j])==len(wordset[i]|wordset[j]):
                    rep=max(rep,len(words[i])*len(words[j]))
        return rep

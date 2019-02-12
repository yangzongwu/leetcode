class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        rep=0
        for k1 in range(len(words)):
            for k2 in range(k1+1,len(words)):
                if not set(words[k1])&set(words[k2]):
                    rep=max(rep,len(words[k1])*len(words[k2]))
        return rep

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x),reverse=True)
        dict_word={}
        for word in words:
            dict_word[word]=set(word)
            
        rep=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                flag2=True
                for ss in dict_word[words[j]]:
                    if ss in dict_word[words[i]]:
                        flag2=False
                        continue
                if flag2==True:
                    rep=max(rep,len(words[i])*len(words[j]))
                    continue
        return rep
        

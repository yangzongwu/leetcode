class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A_list=A.split()
        B_list=B.split()
        dict_word={}
        for word in A_list:
            if word not in dict_word:
                dict_word[word]=1
            else:
                dict_word[word]+=1
        for word in B_list:
            if word not in dict_word:
                dict_word[word]=1
            else:
                dict_word[word]+=1
        rep=[]
        for k in dict_word:
            if dict_word[k]==1:
                rep.append(k)
        return rep

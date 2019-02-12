class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        rep=0
        for k1 in range(len(words)):
            for k2 in range(k1+1,len(words)):
                if not set(words[k1])&set(words[k2]):
                    rep=max(rep,len(words[k1])*len(words[k2]))
        return rep
############################################################
class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        dict_w={}
        for word in words:
            tmp=0
            for s in word:
                tmp=tmp|(1<<(ord(s)-ord('a')))
            #["dbaaffdfa","cccce","fbfdffa"] 注意第一和第三字符一样，长度不一样，所以需要判断
            if tmp in dict_w:
                dict_w[tmp]=max(len(word),dict_w[tmp])
            else:
                dict_w[tmp]=len(word)
            print(dict_w[tmp],dict_w.get(tmp, 0),tmp,word)
        rep=0
        for k1 in dict_w:
            for k2 in dict_w:
                if k1!=k2 and k1&k2==0:
                    rep=max(rep,dict_w[k1]*dict_w[k2])
        return rep

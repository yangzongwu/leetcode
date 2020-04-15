class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queries_int=[]
        words_int=[]
        for query in queries:
            queries_int.append(self.wordToInt(query))
        for word in words:
            words_int.append(self.wordToInt(word))
        words_int.sort()
        rep=[]
        for num in queries_int:
            rep.append(self.getNumberLagerN(num,words_int[::-1]))
        return rep
    
    
    def getNumberLagerN(self,num,words_int):
        cnt=0
        for n in words_int:
            if n>num:
                cnt+=1
            else:
                break
        return cnt
        
    
    def wordToInt(self,word):
        strs=""
        for s in "abcdefghijklmnopqrstuvwxyz":
            if s in word:
                strs=s
                break
        cnt=0
        for s in word:
            if s==strs:
                cnt+=1
        return cnt

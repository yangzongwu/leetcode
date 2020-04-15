class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate=licensePlate.lower()
        dict_licensePlate=self.wordToDict(licensePlate)
        
        rep=''
        for word in words:
            word=word.lower()
            dict_word=self.wordToDict(word)
            if self.isCompletingWord(dict_licensePlate,dict_word):
                if not rep:
                    rep=word
                else:
                    if len(rep)>len(word):
                        rep=word
        return rep
            
    def isCompletingWord(self,dict1,dict2):
        for k in dict1:
            if k not in dict2:
                return False
            if dict1[k]>dict2[k]:
                return False
        return True
    
    def wordToDict(self,licensePlate):
        dict_licensePlate={}
        strs='qwertyuiopasdfghjklzxcvbnm'
        for s in licensePlate:
            if s in strs:
                if s not in dict_licensePlate:
                    dict_licensePlate[s]=1
                else:
                    dict_licensePlate[s]+=1
        return dict_licensePlate

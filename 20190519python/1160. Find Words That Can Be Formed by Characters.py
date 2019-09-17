class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dict_chars=self.stringToDict(chars)
        
        rep=0
        for word in words:
            dict_word=self.stringToDict(word)
            if self.charsContainsWord(dict_chars,dict_word):
                rep+=len(word)
        return rep
                
    def charsContainsWord(self,dict_chars,dict_word):
        for k in dict_word:
            if k not in dict_chars:
                return False
            elif dict_chars[k]<dict_word[k]:
                return False
        return True
            
    def stringToDict(self,word):
        dict_word={}
        for c in word:
            if c not in dict_word:
                dict_word[c]=1
            else:
                dict_word[c]+=1
        return dict_word

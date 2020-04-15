class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1={'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'}
        set_2={'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'}
        set_3={'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'}
        rep=[]
        for word in words:
            if word and word[0] in set_1 and self.isOnOneLine(word,set_1):
                rep.append(word)
            elif word and word[0] in set_2 and self.isOnOneLine(word,set_2):
                rep.append(word)
            elif word and word[0] in set_3 and self.isOnOneLine(word,set_3):
                rep.append(word)
        return rep
    
    def isOnOneLine(self,word,cur_set):
        for c in word:
            if c not in cur_set:
                return False
        return True

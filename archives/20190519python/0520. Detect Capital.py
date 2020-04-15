class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        flag1='qwertyuiopasdfghjklzxcvbnm'
        flag2=flag1.upper()
        if len(word)<=1:
            return True
        if word[0] in flag1:
            for k in range(1,len(word)):
                if word[k] not in flag1:
                    return False
            return True
        else:
            if word[1] in flag1:
                for i in range(2,len(word)):
                    if word[i] not in flag1:
                        return False
            else:
                for j in range(2,len(word)):
                    if word[j] not in flag2:
                        return False
            return True

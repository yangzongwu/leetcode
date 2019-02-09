class Solution:
    def detectCapitalUse(self, word: 'str') -> 'bool':
        if len(word)<=1:
            return True
        if word[0] in 'qwertyuiopasdfghjklzxcvbnm':
            for ss in word[1:]:
                if ss in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                    return False
            return True
        else:
            if word[1] in 'qwertyuiopasdfghjklzxcvbnm':
                for ss in word[2:]:
                    if ss in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                        return False
                return True
            else:
                for ss in word[2:]:
                    if ss in 'qwertyuiopasdfghjklzxcvbnm':
                        return False
                return True

'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rep=[]
        for word in words:
            if word and self.isOneLine(word):
                rep.append(word)
        return rep

    def isOneLine(self,word):
        str1="qwertyuiopQWERTYUIOP"
        str2="asdfghjklASDFGHJKL"
        str3="zxcvbnmZXCVBNM"
        if word[0] in str1 and self.allInLine(word,str1):
            return True
        elif word[0] in str2 and self.allInLine(word,str2):
            return True
        elif word[0] in str3 and self.allInLine(word,str3):
            return True
        return False

    def allInLine(self,word,strs):
        for w in word:
            if w not in strs:
                return False
        return True

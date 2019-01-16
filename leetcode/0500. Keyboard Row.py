'''
Given a List of words, return the words that can be typed using letters of alphabet on only 
one row's of American keyboard like the image below.
 
Example:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 
Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1='qwertyuiop'
        s2='asdfghjkl'
        s3='zxcvbnm'
        rep=[]
        for word in words:
            flag1,flag2,flag3=0,0,0
            for s in word:
                if s in s1:
                    flag1=1
                elif s in s2:
                    flag2=1
                elif s in s3:
                    flag3=1
            if flag1+flag2+flag3==1:
                rep.append(word)
        return rep

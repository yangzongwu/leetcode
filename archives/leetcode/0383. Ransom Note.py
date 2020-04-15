'''
Given an arbitrary ransom note string and another string containing letters from 
all the magazines, write a function that will return true if the ransom note can 
be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict_magazine={}
        for s in magazine:
            if s not in dict_magazine:
                dict_magazine[s]=1
            else:
                dict_magazine[s]+=1
        for s in ransomNote:
            if s not in dict_magazine:
                return False
            else:
                dict_magazine[s]-=1
                if dict_magazine[s]<0:
                    return False
        return True

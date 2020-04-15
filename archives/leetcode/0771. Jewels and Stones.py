'''
You're given strings J representing the types of stones that are jewels, and S representing 
the stones you have.  Each character in S is a type of stone you have.  You want to know how 
many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters 
are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dict_s={}
        for ss in S:
            if ss not in dict_s:
                dict_s[ss]=1
            else:
                dict_s[ss]+=1
        rep=0
        for ss in J:
            if ss in dict_s:
                rep+=dict_s[ss]
        return rep
################################seconde#######################################
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        rep=0
        for ss in S:
            if ss in J:
                rep+=1
        return rep

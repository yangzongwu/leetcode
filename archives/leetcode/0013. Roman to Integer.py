'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, 
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is 
not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making 
four. The same principle applies to the number nine, which is written as IX. There are six instances where 
subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        rep=0
        return self.subRomanToInt(s,rep)
        
    def subRomanToInt(self,s,rep):
        if not s:
            return rep
        if s[0]=='M':
            rep+=1000
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='CM':
            rep+=900
            return self.subRomanToInt(s[2:],rep)
        if s[0]=='D':
            rep+=500
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='CD':
            rep+=400
            return self.subRomanToInt(s[2:],rep)
        
        if s[0]=='C':
            rep+=100
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='XC':
            rep+=90
            return self.subRomanToInt(s[2:],rep)
        if s[0]=='L':
            rep+=50
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='XL':
            rep+=40
            return self.subRomanToInt(s[2:],rep)
        
        if s[0]=='X':
            rep+=10
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='IX':
            rep+=9
            return self.subRomanToInt(s[2:],rep)
        if s[0]=='V':
            rep+=5
            return self.subRomanToInt(s[1:],rep)
        if s[0:2]=='IV':
            rep+=4
            return self.subRomanToInt(s[2:],rep)
        
        if s[0]=='I':
            rep+=1
            return self.subRomanToInt(s[1:],rep)
######################seconde################################################
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rep=0
        for k in range(len(s)):
            if s[k] in 'MDLV':
                rep+=dicts[s[k]]
            if s[k]=='C':
                if k+1<len(s):
                    if s[k+1] in 'DM':
                        rep-=dicts[s[k]]
                    else:
                        rep+=dicts[s[k]]
                else:
                    rep+=dicts[s[k]]
            if s[k]=='X':
                if k+1<len(s):
                    if s[k+1] in 'LC':
                        rep-=dicts[s[k]]
                    else:
                        rep+=dicts[s[k]]
                else:
                    rep+=dicts[s[k]]
            if s[k]=='I':
                if k+1<len(s):
                    if s[k+1] in 'VX':
                        rep-=dicts[s[k]]
                    else:
                        rep+=dicts[s[k]]
                else:
                    rep+=dicts[s[k]]
        return rep

 ############################################################################
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rep=0
        dicts={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        for k in range(len(s)-1):
            if dicts[s[k]]<dicts[s[k+1]]:
                rep-=dicts[s[k]]
            else:
                rep+=dicts[s[k]]
            k+=1
        rep+=dicts[s[-1]]
        return rep

'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
#######time limited####################
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dictp={}
        for ss in p:
            if ss not in dictp:
                dictp[ss]=1
            else:
                dictp[ss]+=1
        
        lenp=len(p)
        rep=[]
        for k in range(len(s)-lenp+1):
            if self.isAnagrams(dictp,s[k:k+lenp]):
                rep.append(k)
        return rep
    
    def isAnagrams(self, dictp, s):
        dictss={}
        for ss in s:
            if ss not in dictss:
                dictss[ss] = 1
            else:
                dictss[ss] += 1

        for keys in dictss:
            if keys not in dictp:
                return False
            if dictp[keys] != dictss[keys]:
                return False
        return True
###############################################################
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        lenp=len(p)
        dictp={}
        for ss in set(p):
            dictp[ss]=p.count(ss)
        
        dicts={}
        for ss in set(s[:lenp-1]):
            dicts[ss]=s[:lenp-1].count(ss)
        
        rep=[]
        for k in range(len(s)-lenp+1):
            if s[k+lenp-1] in dicts:
                dicts[s[k+lenp-1]]+=1
            else:
                dicts[s[k+lenp-1]]=1
                
            if self.isAnagrams(dictp,dicts):
                rep.append(k)
            dicts[s[k]]-=1
                
        return rep
    
    def isAnagrams(self, dictp, dicts):
        for keys in dicts:
            if dicts[keys]!=0:
                if keys not in dictp:
                    return False
                if dictp[keys] != dicts[keys]:
                    return False
        return True
                

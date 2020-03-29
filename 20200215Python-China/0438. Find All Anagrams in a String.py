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
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        
        rep=[]
        dict_p=self.strToDict(p)
        dict_s=self.strToDict(s[:len(p)])
        if self.isSameDict(dict_s,dict_p):
            rep.append(0)

        for k in range(1,len(s)-len(p)+1):
            if s[k+len(p)-1] not in dict_s:
                dict_s[s[k+len(p)-1]]=1
            else:
                dict_s[s[k+len(p)-1]]+=1

            if dict_s[s[k-1]]==1:
                del dict_s[s[k-1]]
            else:
                dict_s[s[k-1]]-=1

            if self.isSameDict(dict_s,dict_p):
                rep.append(k)
        return rep


    def isSameDict(self,dict_s,dict_p):
        for k in dict_s:
            if k not in dict_p or dict_s[k]!=dict_p[k]:
                return False
        return True


    def strToDict(self,p):
        dict_p={}
        for s in p:
            if s not in dict_p:
                dict_p[s]=1
            else:
                dict_p[s]+=1
        return dict_p

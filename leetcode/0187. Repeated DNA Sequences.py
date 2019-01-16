'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<=10:
            return []
        dicts={}
        rep=[]
        for i in range(0,len(s)-9):
            if s[i:i+10] not in dicts:
                dicts[s[i:i+10]]=1
            else:
                if dicts[s[i:i+10]]==1:
                    rep.append(s[i:i+10])
                    dicts[s[i:i+10]]+=1
        return rep
                    

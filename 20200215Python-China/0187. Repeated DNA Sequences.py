'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10:
            return []
        cur=set()
        rep=set()
        for i in range(len(s)-9):
            if s[i:i+10] not in cur:
                cur.add(s[i:i+10])
            else:
                rep.add(s[i:i+10])
        return list(rep)

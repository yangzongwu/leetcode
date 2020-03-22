'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s)==1:
            return [[s]]
            
        rep=[]
        self.getPartitioin(s,rep)
        return rep

    def getPartitioin(self,s,rep):
        for k in range(1,len(s)):
            if s[:k]==s[:k][::-1]:
                for cur in self.partition(s[k:]):
                    rep.append([s[:k]]+cur)
        if s==s[::-1]:
            rep.append([s])

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s)==0:
            return []
        if len(s)==1:
            return [[s]]
        tmp=[]
        rep=[]
    
        for k in range(0,len(s)):
            tmp=[]
            if self.is_palindrome(s[0:k+1]):
                tmp.append([s[0:k+1]])
            for j in range(1,k+1):
                if self.is_palindrome(s[j:k+1]):
                    for curlist in rep[j-1]:
                        tmp.append(curlist+[s[j:k+1]])
            rep.append(tmp)
        return rep[-1]
            
        
        
    def is_palindrome(self,s):
        return s==s[::-1]

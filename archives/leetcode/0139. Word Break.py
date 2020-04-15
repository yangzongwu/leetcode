'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
######################################	Time Limit Exceeded#################################3
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        if s in wordDict:
            return True
        else:
            for k in range(1,len(s)):
                if (s[:k] in wordDict):
                    if self.wordBreak(s[k:], wordDict):
                        return True   
            return False
#######################################################################################
#通常如果递归时间太长的情况下，使用线性规划
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        rep=[]
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                rep.append(True)
            else:
                for j in range(1,i):
                    if rep[j-1] and s[j:i] in wordDict:
                        rep.append(True)
                        break
                else:
                    rep.append(False)
        return rep[-1]

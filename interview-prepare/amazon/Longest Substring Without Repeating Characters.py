'''
Given a string, find the length of the longest substring without repeating characters.

Example
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
Challenge
time complexity O(n)
'''
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        rep=set()
        result=0
        right,left=0,0
        
        while right<len(s):
            while right<len(s) and s[right] not in rep:
                rep.add(s[right])
                right+=1
            if right==len(s):
                result=max(result,len(rep))
                break
            else:
                result=max(result,right-left)
                while s[right] in rep:
                    rep.remove(s[left])
                    left+=1
        return result

'''
Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
Challenge
O(n) time
'''
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k==0:
            return 0
        dicts={}
        result=0
        right,left=0,0
        while right<len(s):
            if len(dicts)<k:
                if s[right] not in dicts:
                    dicts[s[right]]=1
                else:
                    dicts[s[right]]+=1
                right+=1
            else:
                if s[right] in dicts:
                    dicts[s[right]]+=1
                    right+=1
                    
                else:
                    result=max(result,right-left)
                    while True:
                        if dicts[s[left]]==1:
                            del dicts[s[left]]
                            left+=1
                            break
                        else:
                            dicts[s[left]]-=1
                            left+=1
                    dicts[s[right]]=1
                    right+=1
        result=max(result,right-left)
        return result

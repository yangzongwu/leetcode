'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        i=0
        while i<len(strs[0]):
            tmp=strs[0][:i+1]
            flag=1
            for s in strs:
                if s[:i+1]!=tmp:
                    i-=1
                    flag=0
                    break
            if flag==0:
                break
            else:
                i+=1
        return strs[0][:i+1]
#############################seconde#####################################
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]
        minlen=len(strs[0])
        for s in strs:
            minlen=min(minlen,len(s))
        rep=0
        for i in range(minlen):
            flag=strs[0][i]
            for s in strs:
                if s[i]!=flag:
                    return s[:rep]
            rep+=1
        return s[:rep]

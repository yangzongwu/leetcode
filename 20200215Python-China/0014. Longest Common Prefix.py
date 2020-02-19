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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        for k in range(len(strs[0])):
            flag=True
            for strss in strs:
                if k>=len(strss) or strss[k]!=strs[0][k]:
                    flag=False
                    break
            if flag==False:
                return strs[0][:k]
        return strs[0]

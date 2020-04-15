'''
Given a string, you need to reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s=s.split()
        for k in range(len(list_s)):
            list_s[k]=list_s[k][::-1]
        rep=''
        for s in list_s:
            rep=rep+' '+s
        return rep[1:]

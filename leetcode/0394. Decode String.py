'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are 
only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        s_stack = []
        k = 0
        while k < len(s):
            if s[k] in '01234567890':
                i = 0
                while s[k + i] in '1234567890':
                    i += 1
                s_stack.append(int(s[k:k + i]))
                k = k + i
            elif s[k] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPSDFGHJKLAZXCVBNM':
                i = 0
                while k + i < len(s) and s[k + i] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPSDFGHJKLAZXCVBNM':
                    i += 1
                if s_stack and type(s_stack[-1]) == str:
                    tmp=s_stack.pop() + s[k:k + i]
                    s_stack.append(tmp)
                else:
                    s_stack.append(s[k:k + i])
                k = k + i
            elif s[k] == '[':
                k += 1
            else: 
                ss = s_stack.pop() *s_stack.pop()
                if s_stack and type(s_stack[-1]) == str:
                    ss = s_stack.pop() + ss
                    s_stack.append(ss)
                else:
                    s_stack.append(ss)
                k = k + 1
        return s_stack[-1]

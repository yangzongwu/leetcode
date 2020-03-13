'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        s_stack=[]
        k=0
        while k<len(s):
            if s[k] not in '[]':
                if s[k] in '1234567890':
                    i=0
                    while i+k<len(s) and s[i+k] in '1234567890':
                        i+=1
                    s_stack.append(s[k:k+i])
                    k+=i
                else:
                    i=0
                    while i+k<len(s) and s[i+k] not in '1234567890[]':
                        i+=1
                    if not s_stack or s_stack[-1].isdigit():
                        s_stack.append(s[k:k+i])
                    else:
                        s_stack.append(s_stack.pop()+s[k:k+i])
                    k+=i
            elif s[k]==']':
                second=s_stack.pop()
                first=int(s_stack.pop())
                cur=first*second
                if not s_stack or s_stack[-1].isdigit():
                    s_stack.append(cur)
                else:
                    s_stack.append(s_stack.pop()+cur) 
                k+=1
            else:
                k+=1
        return s_stack[-1]

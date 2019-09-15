'''
Given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any bracket.


Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
'''
class Solution:
    def reverseParentheses(self, s: str) -> str:
        s_stack=[]
        l,r=0,0
        while r<len(s):
            if s[r]=='(':
                if r!=l:
                    s_stack.append(s[l:r])
                s_stack.append(s[r])
                l=r+1
            elif s[r]==')':
                cur=s[l:r]
                ss=''
                while ss!='(':
                    ss=s_stack.pop()
                    if ss!='(':
                        cur=ss+cur
                    else:
                        cur=cur[::-1]
                        s_stack.append(cur)
                l=r+1
            r+=1
        if s[-1]!=')':
            s_stack.append(s[l:r])
        rep=""
        for str1 in s_stack:
            rep+=str1
        return rep
        
        
    '''
    def ss:
        if not s:
            return s
        l,r=0,len(s)-1
        while s[l]!='(' and l<r:
            l+=1
        while s[r]!=')' and r>l:
            r-=1
        if l==r:
            return s
        return s[:l]+self.reverseParentheses(s[l+1:r])[::-1]+s[r+1:]
    '''

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.replace(' ','')
        rep=[]
        i=0
        while i<len(s):
            if s[i] not in '+-*/':
                j=1
                while j+i<len(s) and s[i+j] not in '+-*/':
                    j+=1
                rep.append(s[i:i+j])
                i=i+j
            else:
                if s[i] in '+-':
                    rep.append(s[i])
                    i+=1
                else: # s[i]=='*' or '/':
                    left=rep.pop()
                    j=1
                    while j+i<len(s) and s[i+j] not in '+-*/':
                        j+=1
                    right=s[i+1:i+j]
                    if s[i]=='*':                
                        rep.append(int(left)*int(right))
                    else:
                        rep.append(int(left)//int(right))
                    i=i+j
                
        result=0
        for k in range(2,len(rep),2):
            if rep[k-1]=='-':
                rep[k]=-int(rep[k])
        for k in range(0,len(rep),2):
            result+=int(rep[k])
        return result

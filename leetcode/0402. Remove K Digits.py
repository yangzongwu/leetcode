'''
Given a non-negative integer num represented as a string, remove k digits from the number 
so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num_stack=[]
        i,tmp=0,k
        while i < len(num):
            if not num_stack:
                num_stack.append(num[i])
            elif num_stack[-1]<num[i]:
                num_stack.append(num[i])
            else:
                while num_stack and num_stack[-1]>num[i] and tmp>0:
                    num_stack.pop()
                    tmp-=1
                num_stack.append(num[i])
            i+=1
            
        rep=''.join(num_stack)
        while rep and rep[0]=='0':
            rep=rep[1:]
        for i in range(tmp):
            rep=rep[:-1]
        if not rep:
            return '0'
        else:
            return rep

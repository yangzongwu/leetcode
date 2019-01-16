'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed 
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function 
returns 231 − 1 when the division result overflows.
'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0:
            return 0
        flag=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            flag=-1
        dividend,divisor=abs(dividend),abs(divisor)
        list1=[divisor]
        list2=[1]
        while list1[-1]<dividend:
            list1.append(list1[-1]+list1[-1])
            list2.append(list2[-1]+list2[-1])
        tmp=0
        
        for k in range(len(list1)-1,-1,-1):
            if list1[k]>dividend:
                continue
            elif list1[k]==dividend:
                tmp+=list2[k]
                break
            else:
                dividend=dividend-list1[k]
                tmp+=list2[k]
       
        if flag==-1:
            tmp=-tmp
        if tmp>2147483647:
            return 2147483647
        elif tmp<-2147483648:
            return -2147483648
        else:
            return tmp

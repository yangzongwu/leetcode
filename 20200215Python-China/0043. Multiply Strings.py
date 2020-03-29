'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:  
        num1=num1[::-1]
        num2=num2[::-1]
        
        rep=0

        flag1=1
        for i in num1:
            flag2=1
            for j in num2:
                rep+=int(i)*int(j)*flag2*flag1
                flag2*=10
            flag1*=10

        return str(rep)

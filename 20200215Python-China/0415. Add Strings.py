'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str: 
        num1=num1[::-1]
        num2=num2[::-1]
        k=0
        flag=0
        rep=[]
        while k<len(num2) and k<len(num1):
            cur=int(num1[k])+int(num2[k])+flag
            if cur>=10:
                flag=1
                rep.append(cur-10)
            else:
                flag=0
                rep.append(cur)
            k+=1
        
        while k<len(num1):
            cur=int(num1[k])+flag
            if cur>=10:
                flag=1
                rep.append(cur-10)
            else:
                flag=0
                rep.append(cur)
            k+=1

        while k<len(num2):
            cur=int(num2[k])+flag
            if cur>=10:
                flag=1
                rep.append(cur-10)
            else:
                flag=0
                rep.append(cur)
            k+=1

        if flag==1:
            rep.append(1)

        res=0
        for k in range(len(rep)):
           res+=10**k*rep[k]

        return str(res) 

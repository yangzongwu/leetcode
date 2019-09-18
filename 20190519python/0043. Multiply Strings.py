class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rep=0
        for str1 in num1:
            cur=0
            for str2 in num2:
                cur=cur*10+int(str1)*int(str2)
            rep=rep*10+cur
        return str(rep)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1,num2=num2,num1
        num1=num1[::-1]
        num2=num2[::-1]
        rep=""
        flag=0
        for i in range(len(num2)):
            cur=flag+int(num2[i])+int(num1[i])
            if cur>9:
                flag=1
                rep=str(cur-10)+rep
            else:
                flag=0
                rep=str(cur)+rep
        for i in range(len(num2),len(num1)):
            cur=flag+int(num1[i])
            if cur>9:
                flag=1
                rep=str(cur-10)+rep
            else:
                flag=0
                rep=str(cur)+rep
        if flag==1:
            rep='1'+rep
        return rep
                
        

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        rep=[1]
        left=2
        right=num/2
        while left<right:
            if num%left==0:
                rep.append(num//left)
                rep.append(left)
                right=num//left
            else:
                right=num/left
            left+=1
        return num==sum(rep)

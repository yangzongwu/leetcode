class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        rep=[]
        for i in range(0,c+1):
            if i*i<=c:
                rep.append(i*i)
            else:
                break
                
        left,right=0,len(rep)-1
        while left<=right:
            num=rep[left]+rep[right]
            if num==c:
                return True
            elif num<c:
                left+=1
            else:
                right-=1
        return False

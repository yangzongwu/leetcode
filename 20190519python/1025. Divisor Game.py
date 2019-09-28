class Solution:
    def divisorGame(self, N: int) -> bool:
        if N==1:
            return False
        if N==2:
            return True
        dp=[False,True]
        for i in range(3,N+1):
            flag=False
            for k in range(1,i):
                if i%k==0 and dp[-k]==False:
                    dp.append(True)
                    flag=True
                    break
            if flag==False:
                dp.append(False)
        return dp[-1]

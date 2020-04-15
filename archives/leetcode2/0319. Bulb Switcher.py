class Solution:
    def bulbSwitch(self, n: 'int') -> 'int':
        k=1
        cnt=0
        while k*k<=n:
            k+=1
            cnt+=1
        return cnt
        
class Solution:
    def bulbSwitch(self, n: 'int') -> 'int':
        nums=[0]*(n+1)
        for i in range(1,n+1):
            k=1
            while k*i<=n:
                nums[k*i]=nums[k*i]^1
                k+=1
        return sum(nums)

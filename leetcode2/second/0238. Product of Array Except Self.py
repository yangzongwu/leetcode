class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        A=[1]
        cur=1
        for num in nums[:-1]:
            cur*=num
            A.append(cur)
        
        B=[1]
        cur=1
        for num in nums[::-1][:-1]:
            cur*=num
            B.append(cur)
        B=B[::-1]
        
        rep=[]
        for k in range(len(A)):
            rep.append(A[k]*B[k])
        return rep

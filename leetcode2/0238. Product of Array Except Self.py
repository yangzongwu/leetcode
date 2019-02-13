class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repleft=[]
        repright=[]
        res=1
        for num in nums:
            repleft.append(res)
            res=res*num
        res=1
        for num in nums[::-1]:
            repright.append(res)
            res=res*num
        repright=repright[::-1]
        rep=[]
        for i in range(len(nums)):
            rep.append(repleft[i]*repright[i])
        return rep

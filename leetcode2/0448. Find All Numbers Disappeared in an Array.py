class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for k in range(len(nums)):
            while nums[k]!=k+1 and nums[nums[k]-1]!=nums[k]:
                tmp=nums[k]
                nums[k]=nums[tmp-1]
                nums[tmp-1]=tmp
        rep=[]
        for k in range(len(nums)):
            if nums[k]!=k+1:
                rep.append(k+1)
        return rep

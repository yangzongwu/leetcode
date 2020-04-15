class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dictnums={}
        for k in range(len(nums)):
            j=1
            while k+j<len(nums):
                if nums[k+j]>nums[k]:
                    dictnums[nums[k]]=nums[k+j]
                    break
                else:
                    j+=1
            if k+j==len(nums):
                dictnums[nums[k]]=-1
        rep=[]
        for num in findNums:
            rep.append(dictnums[num])
        return rep

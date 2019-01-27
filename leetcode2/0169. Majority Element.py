class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        target=nums[0]
        for num in nums:
            if num==target:
                cnt+=1
            else:
                if cnt==0:
                    target=num
                    cnt=1
                else:
                    cnt-=1
        return target

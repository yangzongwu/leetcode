class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dictnums={}
        for i in range(len(nums)):
            if nums[i] in dictnums:
                if i-dictnums[nums[i]]<=k:
                    return True
            dictnums[nums[i]]=i
        return False    
        

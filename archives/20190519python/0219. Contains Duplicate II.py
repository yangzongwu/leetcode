class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        for left in range(len(nums)-1):
            lo=left
            for right in range(left+1,left+1+k):
                if nums[right]==nums[lo]:
                    if right-lo<=k:
                        return True
                    lo=right
        return False
        '''
        dictnums={}
        for i in range(len(nums)):
            if nums[i] not in dictnums:
                dictnums[nums[i]]=i
            else:
                if i-dictnums[nums[i]]<=k:
                    return True
                dictnums[nums[i]]=i
        return False

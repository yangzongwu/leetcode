class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:
                if nums[mid]>target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<=nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

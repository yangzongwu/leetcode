'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r and nums[l]<=nums[l+1]:
            l+=1
        while r>l and nums[r-1]<=nums[r]:
            r-=1
        
        if r==l:
            return 0
        
        min_val=min(nums[l:r+1])
        max_val=max(nums[l:r+1])
        left=self.findLeftLoc(nums[:l],min_val)
        right=self.findRightLoc(nums[r:],max_val)+r
        return right-left+1

    def findLeftLoc(self,nums,val):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>val:
                r=mid-1
            else:
                l=mid+1
        return l

    def findRightLoc(self,nums,val):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<val:
                l=mid+1
            else:
                r=mid-1
        return r

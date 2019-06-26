class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right-1 and nums[left+1]>=nums[left]:
            left+=1
        
        while right>left+1 and nums[right]>=nums[right-1]:
            right-=1
            
        if left==right:
            return 0
        
        min_val=min(nums[left:right+1])
        max_val=max(nums[left:right+1])
        
        l=self.search_left(nums[:left+1],min_val)
        r=self.search_right(nums[right:],max_val)+right
        
        return r-l+1
    
    def search_left(self,nums,val):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=val:
                left=mid+1
            else:
                right=mid-1
        return left
    
    def search_right(self,nums,val):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<val:
                left=mid+1
            else:
                right=mid-1
        return right

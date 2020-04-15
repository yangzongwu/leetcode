class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        k=left
        while k<=right:
            if nums[k]==1:
                k+=1
            elif nums[k]==0:
                if k==left:
                    k+=1
                    left+=1
                else:
                    nums[k],nums[left]=nums[left],nums[k]        
                    left+=1
            else:# nums[k]==2:
                nums[k],nums[right]=nums[right],nums[k]
                right-=1

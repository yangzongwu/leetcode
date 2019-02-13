class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums)<=2:
            return len(nums)
        left=0
        right=left+1
        flag=1
        while right<len(nums):
            if nums[right]==nums[left]:
                if flag<2:
                    left+=1
                    nums[left],nums[right]=nums[right],nums[left]
                    flag+=1
                    right+=1
                else:
                    right+=1
            else:
                left+=1
                nums[left],nums[right]=nums[right],nums[left]
                flag=1
                right+=1
        return left+1

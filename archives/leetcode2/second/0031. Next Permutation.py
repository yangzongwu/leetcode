class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        #124875
        if not nums or len(nums)==1:
            return
        else:
            r=len(nums)-1
            while r>=1 and nums[r-1]>=nums[r]:
                r-=1
            if r==0:
                nums.reverse()
            else:
                cur=r-1
                r=len(nums)-1
                while nums[r]<=nums[cur]:
                    r-=1
                nums[r],nums[cur]=nums[cur],nums[r]
                nums[cur+1:]=nums[cur+1:][::-1]

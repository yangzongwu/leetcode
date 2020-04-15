class Solution:
    def wiggleSort(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp=sorted(nums)
        lens=len(nums)
        #12345
        #1234
        right=lens-1
        flag=(lens-1)//2
        left=(lens-1)//2
        cnt=0
        while right>flag:
            nums[cnt]=tmp[left]
            nums[cnt+1]=tmp[right]
            left-=1
            right-=1
            cnt+=2
        if left==0:
            nums[cnt]=tmp[left]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        p1=0
        p2=1
        cnt=1
        while p2<len(nums):
            if nums[p2]!=nums[p1]:
                p1+=1
                nums[p1]=nums[p2]
                cnt=1
                p2+=1
            else:
                if cnt==1:
                    cnt+=1
                    p1+=1
                    nums[p1]=nums[p2]
                    p2+=1
                else:
                    p2+=1
        return p1+1

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums_dict={}
        cnt=0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=1
                if k!=0 and num-k in nums_dict and nums_dict[num-k]==1:
                    cnt+=1
                    nums_dict[num-k]-=1
            else:
                if k==0 and nums_dict[num]==1:
                    cnt+=1
                    nums_dict[num]-=1
        return cnt

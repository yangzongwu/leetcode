'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag=0
        cnt=0
        for k in range(len(nums)):
            if nums[k]<0:
                if nums[k]==-2**31:
                    nums[k]=0
                    cnt+=1
                else:
                    nums[k]=abs(nums[k])
                flag+=1     
        flag=flag%3
        
        if cnt==1:
            return -2**31
        
        rep=0
        for i in range(0,32):
            tmp=0
            for k in range(len(nums)):
                tmp+=nums[k]&1
                nums[k]=nums[k]>>1
            rep+=(tmp%3)*(2**i)
        if flag==1:
            return -rep
        else:
            return rep

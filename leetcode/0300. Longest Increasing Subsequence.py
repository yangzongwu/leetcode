'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        
        rep=[1]
        for i in range(1,len(nums)):
            tmp=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    tmp=max(tmp,rep[j]+1)
            rep.append(tmp)
        return max(rep)
###################################################################################
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        rep=[nums[0]]
        for num in nums[1:]:
            if num>rep[-1]:
                rep.append(num)
            elif num<rep[0]:
                rep[0]=num
            else:
                loc=self.find_next_max_num(rep,num)
                rep[loc]=num
        return len(rep)
    
    def find_next_max_num(self,nums,target):
        left=0
        right=len(nums)-1
        while right>=left:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
    

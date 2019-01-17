'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        
        left=nums[0]
        cnt_left=1   
        k=1
        while k <len(nums):
            if nums[k] != left:
                break
            else:
                cnt_left += 1
            k+=1
        if cnt_left == len(nums):
            return [left]

        right = nums[k]
        cnt_right=1
        
        for i in range(k+1,len(nums)):
            if nums[i]==left:
                cnt_left+=1
            elif nums[i]==right:
                cnt_right+=1
            else:
                if cnt_left==0:
                    left=nums[i]
                    cnt_left=1
                elif cnt_right==0:
                    right=nums[i]
                    cnt_right=1
                else:
                    cnt_left-=1
                    cnt_right-=1
        
        cnt_left,cnt_right=0,0
        for num in nums:
            if num==left:
                cnt_left+=1
            if num==right:
                cnt_right+=1
        rep=[]
        if cnt_left>len(nums)/3:
            rep.append(left)
        if cnt_right>len(nums)/3:
            rep.append(right)
        return rep

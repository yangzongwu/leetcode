'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<=2:
            return max(nums)
        
        if nums[1]>nums[0]:
            first=nums[1]
            second=nums[0]
        else:
            first,second=nums[0],nums[1]
        
        if nums[2]>first:
            first,second,third=nums[2],first,second
        elif nums[2]>second:
            first,second,third=first,nums[2],second
        else:
            first,second,third=first,second,nums[2]

        for num in nums[3:]:
            if num>first:
                first,second,third=num,first,second
            elif num>second:
                first,second,third=first,num,second
            elif num>third:
                first,second,third=first,second,num
        return third 


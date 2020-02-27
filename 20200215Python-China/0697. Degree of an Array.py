'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

'''
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        rep=0
        lenth=0
        dict_num={}
        for k in range(len(nums)):
            if nums[k] not in dict_num:
                dict_num[nums[k]]=[k]
            else:
                dict_num[nums[k]].append(k)

            if not rep:
                rep=nums[k]
                lenth=1
            elif len(dict_num[nums[k]])>lenth:
                rep=nums[k]
                lenth=len(dict_num[nums[k]])
            elif len(dict_num[nums[k]])==lenth:
                if dict_num[nums[k]][-1]-dict_num[nums[k]][0]<dict_num[rep][-1]-dict_num[rep][0]:
                    rep=nums[k]
        return dict_num[rep][-1]-dict_num[rep][0]+1

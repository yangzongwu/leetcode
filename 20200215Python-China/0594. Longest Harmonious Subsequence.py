'''
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 

Note: The length of the input array will not exceed 20,000.

'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict_num={}
        for num in nums:
            if num not in dict_num:
                dict_num[num]=1
            else:
                dict_num[num]+=1
        
        rep=0
        for k in dict_num:
            if k+1 in dict_num:
                rep=max(rep,dict_num[k]+dict_num[k+1])
        
        return rep

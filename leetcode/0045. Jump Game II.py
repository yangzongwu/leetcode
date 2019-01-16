
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]

Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

'''
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        tmp = [0]
        len_nums = len(nums)
        for k in range(len_nums):
            if k + nums[k] < len_nums - 1:
                for i in range(len(tmp) - 1, k + nums[k]):
                    tmp.append(tmp[k] + 1)
            else:
                return tmp[k] + 1

    def jump01(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        len_nums=len(nums)
        tmp=[len_nums for k in range(len_nums)]
        tmp[0]=0
        for k in range(len_nums):
            for i in range(k+1,k+nums[k]+1):
                if i<len_nums:
                    if tmp[i]>tmp[k]+1:
                        tmp[i]=tmp[k]+1
        return tmp[-1]

if __name__=='__main__':
    nums=[2,1,1,1,1]
    Test=Solution()
    print(Test.jump(nums))

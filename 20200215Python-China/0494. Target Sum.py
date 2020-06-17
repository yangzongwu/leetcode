### [494\. Target Sum](https://leetcode.com/problems/target-sum/)

Difficulty: **Medium**


You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols `+` and `-`. For each integer, you should choose one from `+` and `-` as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

**Example 1:**

```
Input: nums is [1, 1, 1, 1, 1], S is 3\. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```

**Constraints:**

*   The length of the given array is positive and will not exceed 20.
*   The sum of elements in the given array will not exceed 1000.
*   Your output answer is guaranteed to be fitted in a 32-bit integer.


#### Solution

Language: **Python3**

```python3
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        
        if len(nums)==1:
            if nums[0]==S or -nums[0]==S:
                return 1
            return 0
        
        if nums[0]!=0:
            dict_nums={nums[0]:1,-nums[0]:1}
        else:
            dict_nums={0:2}
            
        for num in nums[1:]:
            tmp={}
            for k,v in dict_nums.items():
                if k+num not in tmp:
                    tmp[k+num]=v
                else:
                    tmp[k+num]+=v
                if -(k+num) not in tmp:
                    tmp[-(k+num)]=v
                else:
                    tmp[-(k+num)]+=v
            dict_nums=tmp
            
        if S in dict_nums:
            return dict_nums[S]
        return 0
```

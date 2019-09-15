'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
'''
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if sum(arr)<=0:
            return self.MaxSumSubArray(arr+arr)%(10**9+ 7)
        if sum(arr)>0 and k>1:
            return ((k-2)*sum(arr)+self.MaxSumSubArray(arr+arr))%(10**9 + 7)
        if k==0:
            return 0
        if k==1:
            return self.MaxSumSubArray(arr)%(10**9+ 7)
        
    def MaxSumSubArray(self,arr):
        if not arr:
            return 0
        if len(arr)==1:
            return max(0,arr[0])
        
        dp=[0]
        cur=0
        for num in arr:
            tmp=dp[-1]+num
            dp.append(max(tmp,0))
            cur=max(cur,dp[-1])
        
        return cur

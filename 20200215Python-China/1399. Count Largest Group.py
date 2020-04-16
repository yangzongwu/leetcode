'''
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5
 

Constraints:

1 <= n <= 10^4
'''
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dict_n={}
        for i in range(1,n+1):
            cur_sum=self.getSumOfDigit(i)
            if cur_sum not in dict_n:
                dict_n[cur_sum]=1
            else:
                dict_n[cur_sum]+=1

        cur=0
        cnt=0
        for k in dict_n:
            if dict_n[k]>cur:
                cnt=1
                cur=dict_n[k]
            elif dict_n[k]==cur:
                cnt+=1
        return cnt

    def getSumOfDigit(self,i):
        cnt=0
        while i>0:
            cnt+=i%10
            i=i//10
        return cnt

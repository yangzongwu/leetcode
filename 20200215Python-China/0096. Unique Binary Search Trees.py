'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[1,1]
        for k in range(2,n+1):
            cur=0
            for i in range(k):
                cur+=dp[i]*dp[k-1-i]
            dp.append(cur)
        return dp[-1]

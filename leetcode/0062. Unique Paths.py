'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 and n==1:
            return 1
        elif m==1 and n>1:
            return self.uniquePaths(m,n-1)
        elif m>1 and n==1:
            return self.uniquePaths(m-1,n)
        else:
            return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
 ########################################################
 class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        rep=[[0 for i in range(n)] for s in range(m)]
        rep[0][0]=1
        for row in range(1,m):
            rep[row][0]=rep[row-1][0]
        for column in range(1,n):
            rep[0][column]=rep[0][column-1]
        for row in range(1,m):
            for column in range(1,n):
                rep[row][column]=rep[row-1][column]+rep[row][column-1]
        return rep[-1][-1]

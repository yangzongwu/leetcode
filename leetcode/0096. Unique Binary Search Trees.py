'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

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
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        listn=[1,1,2]
        for i in range(3,n+1):
            rep=0
            k=0
            while k<len(listn):
                rep+=listn[k]*listn[i-k-1]
                k=k+1
            listn.append(rep)
        return listn[-1]
            
    

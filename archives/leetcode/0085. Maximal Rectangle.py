'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        for colum in range(len(matrix[0])):
            flag=0
            for row in range(len(matrix)):
                if matrix[row][colum]=='1':
                    matrix[row][colum]=flag+1
                    flag= matrix[row][colum]
                else:
                    flag=0
                    matrix[row][colum]=0
        rep=0
        for row in range(len(matrix)):
            rep=max(rep,self.submaximalRectangle(matrix[row]))
        return rep
    
    def submaximalRectangle(self,nums):
        rep=0
        for k in range(len(nums)):
            j=0
            while k+j<len(nums) and nums[k + j]!=0:
                rep=max(rep,(j+1)*min(nums[k:k+j+1]))
                j+=1
        return rep
            
             
                    

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        left=0
        right=m*n-1
        while right>=left:
            mid=(left+right)>>1
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]<target:
                left=mid+1
            else:
                right=mid-1
        return False
                
 #######################################################
 class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        left=0
        right=len(matrix)-1
        while right>=left:
            mid=(right+left)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                right=mid-1
            else:
                left=mid+1
                
        l=0
        r=len(matrix[right])-1
        while r>=l:
            m=(r+l)//2
            if matrix[right][m]==target:
                return True
            elif matrix[right][m]>target:
                r=m-1
            else:
                l=m+1
        return False

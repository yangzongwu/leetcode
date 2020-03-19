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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l,r=0,len(matrix)-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
        
        l0,r0=0,len(matrix[0])-1
        while l0<=r0:
            mid=(l0+r0)//2
            if matrix[r][mid]==target:
                return True
            elif matrix[r][mid]>target:
                r0=mid-1
            else:
                l0=mid+1
        
        return False

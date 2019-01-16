'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
            
        if not matrix or not matrix[0]:
            return []
        elif len(matrix)==1:
            return matrix[0]
        elif len(matrix[0])==1:
            rep=[]
            for num in matrix:
                rep.append(num[0])
            return rep
        else:
            rep=[]
            rep+=matrix[0]
            for k in range(1,len(matrix)-1):
                rep+=[matrix[k][-1]]
            rep+=matrix[-1][::-1]
            for k in range(len(matrix)-2,0,-1):
                rep+=[matrix[k][0]]
            nums=matrix
            nums.pop(0)
            nums.pop(-1)
            for num in nums:
                num.pop(0)
                num.pop(-1)
                
                
            return rep+self.spiralOrder(nums)

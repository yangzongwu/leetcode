'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        123
        456
        789

        1  2  3  4
        12 13 14 5
        11 16 15 6
        10 9  8  7
        '''
        nums=[i for i in range(n**2,0,-1)]
        rep=[[0 for _ in range(n)] for _ in range(n)]
        loc=0
        while n>0:
            self.fillMatrix(rep,loc,n-1,nums)
            n-=2
            loc+=1
        return rep
    
    def fillMatrix(self,matrix,loc,n,nums):
        if n==0:
            matrix[loc][loc]=nums.pop()
            return
        row,col=loc,loc
        for _ in range(n):
            matrix[row][col]=nums.pop()
            col+=1
        for _ in range(n):
            matrix[row][col]=nums.pop()
            row+=1
        for _ in range(n):
            matrix[row][col]=nums.pop()
            col-=1
        for _ in range(n):
            matrix[row][col]=nums.pop()
            row-=1
        
        


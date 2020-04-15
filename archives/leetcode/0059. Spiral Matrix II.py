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
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        rep=[[0 for i in range(n)] for i in range(n)]
        row,column=0,0
        nlist=[i for i in range(1,n**2+1)]
        self.subgenerateMatrix(row,column,rep,nlist,0,n)
        return rep
        
    def subgenerateMatrix(self,row,column,rep,nlist,k,n):
        if k==n**2+1 or rep[row][column]!=0:
            return
        while column<n and rep[row][column]==0:
            rep[row][column]=nlist[k]
            k+=1
            column+=1
        
        column-=1
        row+=1
        while row<n and rep[row][column]==0:
            rep[row][column]=nlist[k]
            k+=1
            row+=1
        
        row-=1
        column-=1
        while column>=0 and rep[row][column]==0:
            rep[row][column]=nlist[k]
            k+=1
            column-=1
        
        column+=1
        row-=1
        while row>=0 and rep[row][column]==0:
            rep[row][column]=nlist[k]
            k+=1
            row-=1
            
        row+=1
        column+=1
        self.subgenerateMatrix(row,column,rep,nlist,k,n)
 ########################################################################################
 class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==1:
            return [[1]]
        rep=[[0 for i in range(n)] for i in range(n)]
        row,column=0,0
        self.subgenerateMatrix(row,column,rep,n,1)
        return rep
        
    def subgenerateMatrix(self,row,column,rep,n,k):
        if rep[row][column]!=0:
            return
        while column<n and rep[row][column]==0:
            rep[row][column]=k
            k+=1
            column+=1
        
        column-=1
        row+=1
        while row<n and rep[row][column]==0:
            rep[row][column]=k
            k+=1
            row+=1
        
        row-=1
        column-=1
        while column>=0 and rep[row][column]==0:
            rep[row][column]=k
            k+=1
            column-=1
        
        column+=1
        row-=1
        while row>=0 and rep[row][column]==0:
            rep[row][column]=k
            k+=1
            row-=1
            
        row+=1
        column+=1
        self.subgenerateMatrix(row,column,rep,n,k)
        

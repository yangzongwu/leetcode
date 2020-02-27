'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

'''
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        N=[[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for row in range(len(M)):
            for col in range(len(M[0])):
                self.refillImage(row,col,M,N)
        return N

    def refillImage(self,row,col,M,N):
        cnt=1
        rep=M[row][col]
        if row-1>=0:
            rep+=M[row-1][col]
            cnt+=1
            if col-1>=0:
                rep+=M[row-1][col-1]
                cnt+=1
            if col+1<len(M[0]):
                rep+=M[row-1][col+1]
                cnt+=1
        if row+1<len(M):
            rep+=M[row+1][col]
            cnt+=1
            if col-1>=0:
                rep+=M[row+1][col-1]
                cnt+=1
            if col+1<len(M[0]):
                rep+=M[row+1][col+1]
                cnt+=1
        if col-1>=0:
            rep+=M[row][col-1]
            cnt+=1
        if col+1<len(M[0]):
            rep+=M[row][col+1]
            cnt+=1
        N[row][col]=rep//cnt

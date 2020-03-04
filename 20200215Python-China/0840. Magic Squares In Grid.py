'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cnt=0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                cnt+=self.isMagicAquares(grid,row,col)
        return cnt

    def isMagicAquares(self,grid,row,col):
        num=set()
        for r in range(3):
            for c in range(3):
                if 0<grid[row+r][col+c]<=9 and grid[row+r][col+c] not in num:
                    num.add(grid[row+r][col+c])
                else:
                    return 0
        target=grid[row][col]+grid[row+1][col]+grid[row+2][col]
        if grid[row][col]+grid[row][col+1]+grid[row][col+2]!=target:
            return 0
        if grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2]!=target:
            return 0
        if grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]!=target:
            return 0
        if grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1]!=target:
            return 0
        if grid[row][col+2]+grid[row+1][col+2]+grid[row+2][col+2]!=target:
            return 0
        if grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]!=target:
            return 0
        if grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]!=target:
            return 0
        return 1

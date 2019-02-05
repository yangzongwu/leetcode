class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        if obstacleGrid[0][0]==1:
            return 0
        
        for row in range(len(obstacleGrid)):
            for column in range(len(obstacleGrid[0])):
                if obstacleGrid[row][column]==1:
                    obstacleGrid[row][column]='X'
        obstacleGrid[0][0]=1
        for row in range(len(obstacleGrid)):
            for column in range(len(obstacleGrid[0])):
                if (row!=0 or column!=0) and obstacleGrid[row][column]!='X':
                    if row==0:
                        if obstacleGrid[row][column-1]!='X':
                            obstacleGrid[row][column]=obstacleGrid[row][column-1]
                        else:
                            obstacleGrid[row][column-1]='X'
                    elif column==0:
                        if obstacleGrid[row-1][column]!='X':
                            obstacleGrid[row][column]=obstacleGrid[row-1][column]
                        else:
                            obstacleGrid[row-1][column]='X'
                    else:
                        
                        if obstacleGrid[row][column-1]!='X' and obstacleGrid[row-1][column]!='X':
                            obstacleGrid[row][column]=obstacleGrid[row][column-1]+obstacleGrid[row-1][column]
                        elif obstacleGrid[row][column-1]=='X' and obstacleGrid[row-1][column]!='X':
                            obstacleGrid[row][column]=obstacleGrid[row-1][column]
                        elif obstacleGrid[row][column-1]!='X' and obstacleGrid[row-1][column]=='X':
                            obstacleGrid[row][column]=obstacleGrid[row][column-1]
                        if obstacleGrid[row][column-1]=='X' and obstacleGrid[row-1][column]=='X':
                            obstacleGrid[row][column]='X'
        if obstacleGrid[-1][-1]=='X':
            return 0
        return obstacleGrid[-1][-1]
                        

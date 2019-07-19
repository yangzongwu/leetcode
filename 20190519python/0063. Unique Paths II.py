class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col]==1:
                    obstacleGrid[row][col]='1'
        
        obstacleGrid[0][0]=1
        
        for row in range(1,len(obstacleGrid)):
            if obstacleGrid[row][0]==0:
                obstacleGrid[row][0]=1
            else:
                break
                
        for col in range(1,len(obstacleGrid[0])):
            if obstacleGrid[0][col]==0:
                obstacleGrid[0][col]=1
            else:
                break
                
        for row in range(1,len(obstacleGrid)):
            for col in range(1,len(obstacleGrid[0])):
                if obstacleGrid[row][col]=='1':
                    continue
                if obstacleGrid[row-1][col]=='1' and obstacleGrid[row][col-1]=='1':
                    obstacleGrid[row][col]='1'
                elif obstacleGrid[row-1][col]!='1' and obstacleGrid[row][col-1]=='1':
                    obstacleGrid[row][col]=obstacleGrid[row-1][col]
                elif obstacleGrid[row-1][col]=='1' and obstacleGrid[row][col-1]!='1':
                    obstacleGrid[row][col]=obstacleGrid[row][col-1]
                else:
                    obstacleGrid[row][col]=obstacleGrid[row-1][col]+obstacleGrid[row][col-1]
                    
        if obstacleGrid[-1][-1]=='1':
            return 0
        return obstacleGrid[-1][-1]
            
        

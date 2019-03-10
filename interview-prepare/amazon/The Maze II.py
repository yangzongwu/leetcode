'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, 
left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at 
the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position 
(excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the 
borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example
Example 1:
	Input:  
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (4,4)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  12
	
	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)

Example 2:
	Input:
	(rowStart, colStart) = (0,4)
	(rowDest, colDest)= (0,0)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Output:  6
	
	Explanation:
	(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)
	
Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border 
of the maze are all walls.
4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        if maze[start[0]][start[1]]==1:
            return -1
        
        cur=[start]
        used=[start]
        step=[0]
        while cur:
            len_cur=len(cur)
            for _ in range(len_cur):
                loc=cur.pop(0)
                cur_step=step.pop(0)
                row,column=loc[0],loc[1]
                if row-1>=0 and maze[row-1][column]==0:
                    row-=1
                    while row>=0 and maze[row][column]==0:
                        row-=1
                    if [row+1,column] not in used:
                        cur.append([row+1,column])
                        used.append([row+1,column])
                        step.append(cur_step+loc[0]-row-1)
                row,column=loc[0],loc[1]
                if column-1>=0 and maze[row][column-1]==0:
                    column-=1
                    while column>=0 and maze[row][column]==0:
                        column-=1
                    if [row,column+1] not in used:
                        cur.append([row,column+1])
                        used.append([row,column+1])
                        step.append(cur_step+loc[1]-column-1)
                row,column=loc[0],loc[1]
                if row+1<len(maze) and maze[row+1][column]==0:
                    row+=1
                    while row<len(maze) and maze[row][column]==0:
                        row+=1
                    if [row-1,column] not in used:
                        cur.append([row-1,column])
                        used.append([row-1,column])
                        step.append(cur_step+row-1-loc[0])
                row,column=loc[0],loc[1]
                if column+1<len(maze[0]) and maze[row][column+1]==0:
                    column+=1
                    while column<len(maze[0]) and maze[row][column]==0:
                        column+=1
                    if [row,column-1] not in used:
                        cur.append([row,column-1])
                        used.append([row,column-1])
                        step.append(cur_step+column-1-loc[1])
            if destination in cur:
                k=0
                while k<len(cur):
                    if cur[k]==destination:
                        return step[k]
                    k+=1
        return -1

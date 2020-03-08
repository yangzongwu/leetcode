'''
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
 

Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.

'''

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:             
        dict_obs={}
        for obs in obstacles:
            if obs[0] not in dict_obs:
                dict_obs[obs[0]]=set()
            dict_obs[obs[0]].add(obs[1])
        x,y=0,0
        flag_x,flag_y=0,1
        rep=0
        for cmd in commands:
            if cmd==-1:
                if flag_x==1:
                    flag_x=0
                    flag_y=-1
                elif flag_x==-1:
                    flag_x=0
                    flag_y=1
                elif flag_y==1:
                    flag_x=1
                    flag_y=0
                elif flag_y==-1:
                    flag_x=-1
                    flag_y=0
            elif cmd==-2:
                if flag_x==1:
                    flag_x=0
                    flag_y=1
                elif flag_x==-1:
                    flag_x=0
                    flag_y=-1
                elif flag_y==1:
                    flag_x=-1
                    flag_y=0
                elif flag_y==-1:
                    flag_x=1
                    flag_y=0
            else:
                if flag_x==1:
                    for _ in range(cmd):
                        if (x+1 not in dict_obs) or (y not in dict_obs[x+1]):
                            x+=1
                        else:
                            break
                elif flag_x==-1:
                    for _ in range(cmd):
                        if (x-1 not in dict_obs) or (y not in dict_obs[x-1]):
                            x-=1
                        else:
                            break
                elif flag_y==1:
                    for _ in range(cmd):
                        if (x not in dict_obs) or (y+1 not in dict_obs[x]):
                            y+=1
                        else:
                            break
                elif flag_y==-1:
                    for _ in range(cmd):
                        if (x not in dict_obs) or (y-1 not in dict_obs[x]):
                            y-=1
                        else:
                            break
            rep=max(rep,x**2+y**2)
        return rep

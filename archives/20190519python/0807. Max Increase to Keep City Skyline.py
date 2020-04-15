class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        l_to_r=[]
        t_to_b=[]
        for cur_list in grid:
            l_to_r.append(max(cur_list))
        
        for k in range(len(grid[0])):
            rep=grid[0][k]
            for j in range(len(grid)):
                rep=max(rep,grid[j][k])
            t_to_b.append(rep)
            
        result=[]
        for cur_l_to_r_val in l_to_r:
            tmp=[]
            for cur_t_to_b_val in t_to_b:
                tmp.append(min(cur_l_to_r_val,cur_t_to_b_val))
            result.append(tmp)
            
        rep=0
        for row in range(len(result)):
            for col in range(len(result[0])):
                rep+=result[row][col]-grid[row][col]
        return rep

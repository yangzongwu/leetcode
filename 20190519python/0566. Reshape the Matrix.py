class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0])!=r*c:
            return nums
        rep=[[0]*c for i in range(r)]
        
        cur=[]
        for row in range(len(nums)):
            for col in range(len(nums[0])):
                cur.append(nums[row][col])
        
        
        for row in range(len(rep)):
            for col in range(len(rep[0])):
                rep[row][col]=cur[row*len(rep[0])+col]
        
        return rep
        

class Solution:
    def matrixReshape(self, nums: 'List[List[int]]', r: 'int', c: 'int') -> 'List[List[int]]':
        if r*c!=len(nums)*len(nums[0]):
            return nums
        rep=[[0 for _ in range(c)] for _ in range(r)]
        rowrep,columnrep,rownums,columnnums=0,0,0,0
        while rowrep<r and columnrep<c:
            rep[rowrep][columnrep]=nums[rownums][columnnums]
            if columnrep==c-1:
                columnrep=0
                rowrep+=1
            else:
                columnrep+=1
                
            if columnnums==len(nums[0])-1:
                columnnums=0
                rownums+=1
            else:
                columnnums+=1
        return rep

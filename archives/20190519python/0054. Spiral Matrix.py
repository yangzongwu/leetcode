class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        rep=[]
        self.getSpiralOrder(matrix,rep,0,len(matrix)-1,0,len(matrix[0])-1)
        return rep
    
    
    def getSpiralOrder(self,matrix,rep,up,down,left,right):
        if left>right or up>down:
            return
        if left==right and up==down:
            rep.append(matrix[up][left])
        elif left<right and up==down:
            for col in range(left,right+1):
                rep.append(matrix[up][col])
        elif left==right and up<down:
            for row in range(up,down+1):
                rep.append(matrix[row][left])
        else:
            for col in range(left,right+1):
                rep.append(matrix[up][col])
            for row in range(up+1,down+1):
                rep.append(matrix[row][right])
            for col in range(right-1,left-1,-1):
                rep.append(matrix[down][col])
            for row in range(down-1,up,-1):
                rep.append(matrix[row][left])
            self.getSpiralOrder(matrix,rep,up+1,down-1,left+1,right-1)
            return

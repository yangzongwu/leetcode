class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rep=[[0]*len(M[0]) for k in range(len(M))]
        
        for row in range(len(rep)):
            for col in range(len(rep[0])):
                rep[row][col]=self.cal_soomther(M,row,col)
        
        return rep
    
    def cal_soomther(self,M,row,col):
        cnt=1
        res=M[row][col]
        if row-1>=0:
            res+=M[row-1][col]
            cnt+=1
            if col-1>=0:
                res+=M[row-1][col-1]
                cnt+=1
            if col+1<len(M[0]):
                res+=M[row-1][col+1]
                cnt+=1
        if row+1<len(M):
            res+=M[row+1][col]
            cnt+=1
            if col-1>=0:
                res+=M[row+1][col-1]
                cnt+=1
            if col+1<len(M[0]):
                res+=M[row+1][col+1]
                cnt+=1
        if col-1>=0:
            res+=M[row][col-1]
            cnt+=1
        if col+1<len(M[0]):
            res+=M[row][col+1]
            cnt+=1
        return res//cnt

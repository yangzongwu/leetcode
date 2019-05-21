class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rep=[]
        if numRows==0:
            return rep
        rep.append([1])
        if numRows==1:
            return rep
        rep.append([1,1])
        if numRows==2:
            return rep
        while(numRows>2):
            prev=rep[-1]
            cur=[1]
            for k in range(len(prev)-1):
                cur.append(prev[k]+prev[k+1])
            cur.append(1)
            rep.append(cur)
            numRows-=1
        return rep
            

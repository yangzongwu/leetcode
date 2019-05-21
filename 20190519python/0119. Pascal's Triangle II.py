class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        
        prev=[1,1]
        while(rowIndex>1):            
            cur=[1]
            for k in range(len(prev)-1):
                cur.append(prev[k]+prev[k+1])
            cur.append(1)
            prev=cur
            rowIndex-=1
        return prev
            

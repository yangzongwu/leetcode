class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rep=[]
        
        for k in range(numRows):
            rep.append(s[k])
            
        for k in range(numRows,len(s)):
            cur=k%(numRows+numRows-2)
            if cur<numRows:
                rep[cur]+=s[k]
            else:
                rep[numRows*2-cur-2]+=s[k]
        res=""
        for s in rep:
            res+=s
        return res

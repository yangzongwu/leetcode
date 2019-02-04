class Solution(object):
    def convert(self, s,numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        
        rep=['']*numRows
        k=0
        while k<len(s):
            if (k%(numRows+numRows-2))<numRows:
                rep[k%(numRows+numRows-2)]+=s[k]
                k+=1
            else:# (k%(numRows+numRows-2))<numRows+numRows-2:
                rep[numRows-2-k%(numRows+numRows-2)]+=s[k]
                k+=1
        res=''
        for s in rep:
            res+=s
        return res
                

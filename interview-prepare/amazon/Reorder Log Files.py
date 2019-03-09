class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitlog=[]
        strlog=[]
        for log in logs:
            loglist=log.split(' ')
            if loglist[1].isalpha():
                strlog.append([' '.join(loglist[1:]),loglist[0]])
            else:
                digitlog.append(log)
                
        
        strlog.sort()
        rep=[]
        for log in strlog:
            rep.append(log[1]+' '+log[0])
        rep+=digitlog
        return rep
        

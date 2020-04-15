class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour=[1,2,4,8]
        minute=[1,2,4,8,16,32]
        
        rep=[]
        for i in range(num+1):
            if i<=4 and 0<=num-i<=6:
                hourlist=self.subreadBinaryWatch(hour,i)
                minutelist=self.subreadBinaryWatch(minute,num-i)
                for h in hourlist:
                    for m in minutelist:
                        if h<12 and m<60:
                            if m<10:
                                m1='0'+str(m)
                            else:
                                m1=str(m)
                            rep.append(str(h)+':'+m1)
        return rep
    
    def subreadBinaryWatch(self,num,k):
        rep=[]
        def dfs(num,k,res,rep):
            if k==0:
                rep.append(res)
            if not num or k<0:
                return
            for i in range(len(num)):
                dfs(num[i+1:],k-1,res+num[i],rep)
        dfs(num,k,0,rep)
        return rep

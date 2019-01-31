class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour=[8,4,2,1]
        minute=[32,16,8,4,2,1]
        rep=[]
        for k in range(num+1):
            if k<=4 and num-k<=6:
                s1=self.number_lights_on(hour,k)
                s2=self.number_lights_on(minute,num-k)
                for ss1 in s1:
                    for ss2 in s2:
                        if ss1<12 and ss2<60:
                            tmp1=str(ss1)
                            tmp2=str(ss2)
                            if ss2<10:
                                tmp2='0'+tmp2
                            rep.append(tmp1+':'+tmp2)
        return rep
    
    def number_lights_on(self,nums,k):
        if k == 0:
            return [0]
        
        rep=[]
        def dfs(nums,k,res,rep):
            if k==0:
                rep.append(res)
            elif not nums:
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:],k-1,res+nums[i],rep)
                
        dfs(nums,k,0,rep)
        return rep
                

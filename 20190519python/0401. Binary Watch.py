class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        h=[1,2,4,8]
        m=[1,2,4,8,16,32]
        if num==0:
            return ["0:00"]
        rep=[]
        for n_hour in range(max(0,num-6),min(num,3)+1):
            hour_list=self.subReadBinaryWatch(h,n_hour,'h')
            min_list=self.subReadBinaryWatch(m,num-n_hour,'m')
            for h_str in hour_list:
                for m_str in min_list:
                    hh=str(h_str)
                    if m_str<10:
                        mm='0'+str(m_str)
                    else:
                        mm=str(m_str)
                    rep.append(hh+":"+mm)
        return rep
        
    def subReadBinaryWatch(self,nums,k,flag):
        if k==0:
            return [0]
        rep=[]
        def dfs(nums,k,rep,res,flag):
            if k==0:
                if flag=='h':
                    if res<12:
                        rep.append(res)
                else:
                    if res<60:
                        rep.append(res)
            if not nums:
                return
            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:],k-1,rep,res+nums[i],flag)
                
        dfs(nums,k,rep,0,flag)
        return rep

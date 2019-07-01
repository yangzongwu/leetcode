class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums)==1:
            return nums
        
        FN,SN=None,None
        Fcnt,Scnt=0,0
        for num in nums:
            if FN!=None and SN!=None:
                if num==FN:
                    Fcnt+=1
                elif num==SN:
                    Scnt+=1
                else:
                    if Fcnt==0:
                        FN=num
                        Fcnt=1
                    elif Scnt==0:
                        SN=num
                        Scnt=1
                    else:
                        Fcnt-=1
                        Scnt-=1
            elif FN==None and SN!=None:
                if SN==num:
                    Scnt+=1
                else:
                    FN=num
                    Fcnt=1
            elif FN!=None and SN==None:
                if FN==num:
                    Fcnt+=1
                else:
                    SN=num
                    Scnt=1
            else:
                FN=num
                Fcnt=1
        
        
        cnt_FN=0
        cnt_SN=0
        cnt=0
        for num in nums:
            if num==FN:
                cnt_FN+=1
            if num==SN:
                cnt_SN+=1
            cnt+=1
        
        rep=[]
        if cnt_FN!=0 and cnt/cnt_FN<3:
            rep.append(FN)
        if cnt_SN!=0 and cnt/cnt_SN<3:
            rep.append(SN)
        return rep

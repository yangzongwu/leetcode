class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dictA=self.listToDict(A)
        dictB=self.listToDict(B)
        dictC=self.listToDict(C)
        dictD=self.listToDict(D)
        
        dictAB={}
        for kA in dictA:
            for kB in dictB:
                if kA+kB not in dictAB:
                    dictAB[kA+kB]=dictA[kA]*dictB[kB]
                else:
                    dictAB[kA+kB]+=dictA[kA]*dictB[kB]
        
        rep=0
        for kC in dictC:
            for kD in dictD:
                if -kC-kD in dictAB:
                    rep+=dictAB[-kC-kD]*dictC[kC]*dictD[kD]
        return rep
        
    def listToDict(self,nums):
        dict_num={}
        for num in nums:
            if num not in dict_num:
                dict_num[num]=1
            else:
                dict_num[num]+=1
        return dict_num

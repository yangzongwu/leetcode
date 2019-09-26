class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        rep=[]
        if len(A)==1:
            for s in A:
                rep.append(s)
            return rep
        
        A_list=[]
        for s in A:
            A_list.append(self.stringToDict(s))
            
        for cur in A_list[0]:
            num=self.sameVal(A_list,cur)
            if num>0:
                for _ in range(num):
                    rep.append(cur)
        return rep
    
    def sameVal(self,Alist,cur):
        rep=Alist[0][cur]
        for cur_dict in Alist[1:]:
            if cur not in cur_dict:
                return 0
            else:
                rep=min(rep,cur_dict[cur])
        return rep
        
        
    def stringToDict(self,s):
        dict_s={}
        for ss in s:
            if ss not in dict_s:
                dict_s[ss]=1
            else:
                dict_s[ss]+=1
        return dict_s

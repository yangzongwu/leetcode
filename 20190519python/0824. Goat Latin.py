class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_list=S.split(" ")
        str_end='a'
        for k in range(len(s_list)):
            s_list[k]=self.getGoatLation(s_list[k],str_end)
            str_end+='a'
        rep=""
        for ss in  s_list:
            rep+=' '+ss
        return rep[1:]
    
    def getGoatLation(self,s1,s2):
        if s1[0] in 'aeiouAEIOU':
            return s1+'ma'+s2
        else:
            return s1[1:]+s1[0]+'ma'+s2
        

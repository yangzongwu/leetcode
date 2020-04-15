class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dict_f={}
        for i in range(1,f+1):
                dict_f[i]=1
                
        while d>1:
            dict_s={} 
            for i in range(1,f+1):
                for key in dict_f:
                    if i+key not in dict_s:
                        dict_s[i+key]=dict_f[key]
                    else:
                        dict_s[i+key]+=dict_f[key]
            dict_f=dict_s
            d-=1
        if target in dict_f:
            return dict_f[target]%(10**9 + 7)
        else:
            return 0
        
        
            
        

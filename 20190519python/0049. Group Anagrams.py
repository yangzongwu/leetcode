class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs={}
        for ss in strs:
            cur_str_list=[x for x in ss]
            cur_str_list.sort()
            cur_str=str(cur_str_list)
            
            if cur_str not in dict_strs:
                dict_strs[cur_str]=[ss]
            else:
                dict_strs[cur_str].append(ss)
                
        rep=[]
        for key in dict_strs:
            rep.append(dict_strs[key])
        
        return rep

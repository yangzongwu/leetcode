class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_list={}
        for k in range(len(list1)):
            dict_list[list1[k]]=k
        
        rep=[]
        cnt=len(list1)+len(list2)
        
        for k in range(len(list2)):
            if list2[k] in dict_list:
                if k+dict_list[list2[k]]<cnt:
                    cnt=k+dict_list[list2[k]]
                    rep=[list2[k]]
                elif k+dict_list[list2[k]]==cnt:
                    rep.append(list2[k])
        
        return rep

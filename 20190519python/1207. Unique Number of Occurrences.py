class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr={}
        for num in arr:
            if num not in dict_arr:
                dict_arr[num]=1
            else:
                dict_arr[num]+=1
        
        rep=set()
        cnt=0
        for k in dict_arr:
            cnt+=1
            rep.add(dict_arr[k])
        
        return len(rep)==cnt

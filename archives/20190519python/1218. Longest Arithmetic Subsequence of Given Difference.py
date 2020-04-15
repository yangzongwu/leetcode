class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dict_arr={}
        for k in range(len(arr)):
            if arr[k] not in dict_arr:
                dict_arr[arr[k]]=[k]
            else:
                dict_arr[arr[k]].append(k)
        
        rep=0
        used_arr=set()
        
        for k in range(len(arr)):
            if arr[k] not in used_arr:
                cnt=1
                next_number=arr[k]+difference
                loc=k
                while next_number in dict_arr and dict_arr[next_number][-1]>loc:
                    used_arr.add(next_number)
                    for i in dict_arr[next_number]:
                        if i>loc:
                            loc=i
                            break
                    cnt+=1
                    next_number+=difference
                rep=max(rep,cnt)
        
        return rep

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        rep=[[arr[0],arr[1]]]
        gap=arr[1]-arr[0]
        for k in range(1,len(arr)-1):
            cur_gap=arr[k+1]-arr[k]
            if cur_gap<gap:
                rep=[[arr[k],arr[k+1]]]
                gap=cur_gap
            elif cur_gap==gap:
                rep.append([arr[k],arr[k+1]])
            else:
                continue
        return rep
                

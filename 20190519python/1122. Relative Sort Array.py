class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict_sort={}
        cnt=1
        for num in arr2:
            dict_sort[num]=cnt
            cnt+=1
        for num in arr1:
            if num not in dict_sort:
                dict_sort[num]=cnt+1
        
        arr1.sort()
        arr1.sort(key=lambda x: dict_sort[x])
        
        return arr1

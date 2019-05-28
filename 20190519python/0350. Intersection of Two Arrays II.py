class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_num={}
        for num in nums1:
            if num not in dict_num:
                dict_num[num]=1
            else:
                dict_num[num]+=1
        rep=[]
        for num in nums2:
            if num in dict_num and dict_num[num]>0:
                rep.append(num)
                dict_num[num]-=1
        return rep

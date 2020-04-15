class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dicts={}
        for num in nums1:
            if num not in dicts:
                dicts[num]=1
            else:
                dicts[num]+=1
        rep=[]
        for num in nums2:
            if num not in dicts:
                continue
            else:
                if dicts[num]>0:
                    dicts[num]-=1
                    rep.append(num)
        return rep

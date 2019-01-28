class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=list(set(nums2))
        rep=[]
        for num in nums2:
            if num in nums1:
                rep.append(num)
        return rep

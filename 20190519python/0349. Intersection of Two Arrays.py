class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rep=[]
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        for num in nums2_set:
            if num in nums1_set:
                rep.append(num)
        return rep

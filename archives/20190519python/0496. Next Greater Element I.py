class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_nextmax_dict={}
        for i in range(len(nums2)):
            target=nums2[i]
            k=i+1
            while k<len(nums2):
                if nums2[k]>target:
                    nums2_nextmax_dict[target]=nums2[k]
                    break
                k+=1
            if k==len(nums2):
                nums2_nextmax_dict[target]=-1
        rep=[]
        for num in nums1:
            rep.append(nums2_nextmax_dict[num])
        return rep

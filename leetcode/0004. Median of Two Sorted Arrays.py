'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len=len(nums1)+len(nums2)
        if total_len%2!=0:
            rep=self.findKnumberSortedArrays(nums1,nums2,total_len//2)
        else:
            rep1=self.findKnumberSortedArrays(nums1,nums2,total_len//2-1)
            rep2=self.findKnumberSortedArrays(nums1,nums2,total_len//2)
            rep=(rep1+rep2)/2
        return rep
    
    def findKnumberSortedArrays(self,nums1,nums2,k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k==0 and nums1 and nums2:
            return min(nums1[0],nums2[0])
        
        len1,len2=len(nums1),len(nums2)
        if nums1[len1//2]>nums2[len2//2]:
            if k>len1//2+len2//2:
                return self.findKnumberSortedArrays(nums1,nums2[len2//2+1:],k-len2//2-1)
            else:
                return self.findKnumberSortedArrays(nums1[:len1//2],nums2,k)
        else:
            if k>len1//2+len2//2:
                return self.findKnumberSortedArrays(nums1[len1//2+1:],nums2,k-len1//2-1)
            else:
                return self.findKnumberSortedArrays(nums1,nums2[:len2//2],k)

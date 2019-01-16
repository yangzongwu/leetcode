'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p_nums1=0
        p_nums2=0
        flag=0
        while p_nums2<n:
            if flag<m:
                if nums2[p_nums2]<nums1[p_nums1]:
                    nums1.insert(p_nums1,nums2[p_nums2])
                    nums1.pop()
                    p_nums1+=1
                    p_nums2+=1
                else:
                    p_nums1+=1
                    flag+=1
            else:
                for s in nums2[p_nums2:]:
                    nums1.pop()
                for s in nums2[p_nums2:]:
                    nums1.append(s)
                break
########################################################################
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
        if m==0:
            for s in range(n):
                nums1[s]=nums2[s]
                

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A
        if A[0]>=0:
            return self.getSquares(A)
        if A[0]<0:
            if A[-1]<0:
                A=self.getSquares(A)
                return A[::-1]
            
            k=0
            while k<len(A) and A[k]<0:
                k+=1
            
            nums1=self.getSquares(A[:k][::-1])
            nums2=self.getSquares(A[k:])
        return self.getsortedArray(nums1,nums2)
    
    def getsortedArray(self,nums1,nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        rep=[]
        k1,k2=0,0
        while k1<len(nums1) and k2<len(nums2):
            if nums1[k1]<nums2[k2]:
                rep.append(nums1[k1])
                k1+=1
            else:
                rep.append(nums2[k2])
                k2+=1
        while k1<len(nums1):
            rep.append(nums1[k1])
            k1+=1
        while k2<len(nums2):
            rep.append(nums2[k2])
            k2+=1
        return rep
            
    def getSquares(self,A):
        for k in range(len(A)):
            A[k]=A[k]*A[k]
        return A

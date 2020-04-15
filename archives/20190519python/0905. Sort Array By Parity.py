class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left,right=0,0
        while right<len(A) and left<len(A):
            while left<len(A) and A[left]%2==0:
                left+=1
            right=left
            while right<len(A) and A[right]%2!=0:
                right+=1
            if left==len(A) or right==len(A):
                break
            A[left],A[right]=A[right],A[left]
            
            right+=1
            left+=1
        return A

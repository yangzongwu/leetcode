class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        left=0
        right=len(A)-1
            
        while left<right:
            if A[left]%2==0:
                left+=1
            else:
                A[left],A[right]=A[right],A[left]
                right-=1
        return A

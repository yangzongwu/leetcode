'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[-1]<0:
            for k in range(len(A)):
                A[k]=A[k]**2
            return A[::-1]
            
        B=[]
        cur=0
        for k in range(len(A)):
            if A[k]<0:
                B.append(A[k]**2)
                A[k]=0
            else:
                cur=k
                break
        for k in range(cur, len(A)):
            A[k]=A[k]**2
        
        B=B[::-1]
        lA=cur
        lB=0

        cur=0
        while lB<len(B) and lA<len(A):
            if A[lA]<B[lB]:
                A[cur]=A[lA]
                lA+=1
            else:
                A[cur]=B[lB]
                lB+=1
            cur+=1
        
        if lA==len(A):
            while lB<len(B):
                A[cur]=B[lB]
                cur+=1
                lB+=1
        
        return A


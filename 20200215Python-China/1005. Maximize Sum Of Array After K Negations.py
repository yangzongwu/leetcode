'''
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.

 

Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
 

Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100

'''
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        cur=0
        while K>0:
            if A[cur]<0:
                A[cur]=-A[cur]
                cur+=1
                K-=1
            else:
                K=K%2
                if K==1:
                    if cur==0:
                        A[cur]=-A[cur]
                    else:
                        if A[cur]>A[cur-1]:
                            A[cur-1]=-A[cur-1]
                        else:
                            A[cur]=-A[cur]
                    K-=1
        return sum(A)



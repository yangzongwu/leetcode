###################################Time Limit Exceeded########################################
class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        len_A=len(A)
        if not A:
            return 0
        if K>=len_A:
            if 0 in A:
                if sum(A)!=0:
                    return -1
                else:
                    return 1
            else:
                return 0
        cnt=0
        i=0
        while i<len_A-K+1:
            if A[i]==0:
                cnt+=1
                for m in range(i,i+K):
                    A[m]=A[m]^1
            i+=1
        for j in range(i,len(A)):
            if A[j]==0:
                return -1
        return cnt

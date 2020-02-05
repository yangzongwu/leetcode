class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if len(A)!=len(B):
            return False
            
        total_len=len(A)
        for i in range(total_len):
            if A[i]==B[0]:
                if A[i:]==B[:(total_len-i)] and A[:i]==B[(total_len-i):]:
                    return True
        return False

'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

'''
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if B in A:
            return 1

        k=len(B)//len(A)
        cur=A*k
        if B in cur:
            return k
        if B in cur+A:
            return k+1
        if B in cur+A+A:
            return k+2
        return -1
        




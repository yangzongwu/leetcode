'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
'''
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        rep=[]
        for h1 in range(len(A)):
            if A[h1]<=2:
                for h2 in range(len(A)):
                    if h1!=h2 and A[h1]*10+A[h2]<24:
                        for m1 in range(len(A)):
                            if m1!=h1 and m1!=h2 and A[m1]<6:
                                for m2 in range(len(A)):
                                    if m2!=m1 and m2!=h1 and m2!=h2 and A[m1]*10+A[m2]<60:
                                        if not rep or 60*(10*A[h1]+A[h2])+10*A[m1]+A[m2]>60*(10*rep[0]+rep[1])+10*rep[2]+rep[3]:
                                            rep=[A[h1],A[h2],A[m1],A[m2]]
                                       
        if not rep:
            return ""
        return str(rep[0])+str(rep[1])+":"+str(rep[2])+str(rep[3])

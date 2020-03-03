'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        loc=[]
        for k in range(len(S)):
            if S[k]==C:
                loc.append(k)
        
        rep=[]
        k_s=0
        k_c=0
        while k_s<len(S):
            if k_s<=loc[0]:
                rep.append(loc[0]-k_s)
            elif k_s>=loc[-1]:
                rep.append(k_s-loc[-1])
            else:
                while k_s>loc[k_c]:
                    k_c+=1
                rep.append(min(k_s-loc[k_c-1],loc[k_c]-k_s))
            k_s+=1

        return rep

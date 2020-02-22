'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA=0
        for k in range(len(s)):
            if s[k]=='A':
                cntA+=1
                if cntA==2:
                    return False
            elif s[k]=='L':
                if k+2<len(s) and s[k+1]==s[k+2]=='L':
                    return False
        return True

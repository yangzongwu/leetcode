'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

'''
class Solution:
    def countSegments(self, s: str) -> int:
        s_list=s.split(" ")
        cnt=0
        for ss in s_list:
            if ss:
                cnt+=1
        return cnt

'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s_list=self.countStrToList(s)
        rep=0
        for k in range(1,len(s_list)):
            rep+=min(s_list[k],s_list[k-1])
        return rep



    def countStrToList(self,s):
        rep=[]
        k=0
        while k<len(s):
            target=s[k]
            i=1
            while k+i<len(s) and s[k+i]==target:
                i+=1
            rep.append(i)
            k=k+i
        return rep
    

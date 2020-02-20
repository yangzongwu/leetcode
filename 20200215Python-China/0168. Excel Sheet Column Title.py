'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        strs="abcdefghijklmnopqrstuvwxyz"
        strs=strs.upper()
        dict_s={}
        for k in range(len(strs)):
            dict_s[k+1]=strs[k]

        rep=""    
        while n>0:
            if n%26!=0:
                rep=dict_s[n%26]+rep
                n=(n-n%26)//26
            else:
                rep='Z'+rep
                n=n//26-1
        return rep

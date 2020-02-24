'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].

'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
            
        flag=True
        if num<0:
            flag=False
            num=-num
        
        rep=""
        while num>0:
            rep=str(num%7)+rep
            num=(num-num%7)//7
        
        if flag==False:
            rep='-'+rep
        return rep

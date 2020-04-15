'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        rep=[[1]]
        while numRows>1:
            cur=[1]
            i=0
            while i<len(rep[-1])-1:
                cur.append(rep[-1][i]+rep[-1][i+1])
                i+=1
            cur.append(1)
            rep.append(cur)
            numRows-=1
            
        return rep

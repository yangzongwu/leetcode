'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

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
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return[[1],[1,1]]
        rep=[[1],[1,1]]
        prev=[1,1]
        for k in range(3,numRows+1):
            cur=[1]
            for k in range(len(prev)-1):
                cur.append(prev[k]+prev[k+1])
            cur.append(1)
            prev=cur
            rep.append(cur)
        return rep

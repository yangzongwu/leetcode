'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Example:

Input: 3
Output: [1,3,3,1]
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        prev=[1,1]
        for k in range(2,rowIndex+1):
            cur=[1]
            for k in range(len(prev)-1):
                cur.append(prev[k]+prev[k+1])
            cur.append(1)
            prev=cur
        return prev

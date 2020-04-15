'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        rep=[1,1]
        while rowIndex>1:
            cur=[1]
            i=0
            while i<len(rep)-1:
                cur.append(rep[i]+rep[i+1])
                i+=1
            cur.append(1)
            rowIndex-=1
            rep=cur
        return rep

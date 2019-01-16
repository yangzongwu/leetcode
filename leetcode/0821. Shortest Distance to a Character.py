'''
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        rep = []
        left = 0
        while S[left] != C:
            left += 1
        right = left

        # before
        if left > 0:
            tmp = left
            while tmp > 0:
                rep.append(tmp)
                tmp -= 1
        # mid
        rep.append(0)
        right = left + 1
        while right < len(S):
            while  right < len(S) and S[right] != C:
                right += 1
            if right<len(S) and right - left - 1>0:
                midgap = right - left - 1
                if midgap % 2 == 0:
                    for k in range(1, midgap // 2+1):
                        rep.append(k)
                    for k in range(midgap // 2, 0, -1):
                        rep.append(k)
                else:
                    for k in range(1, midgap // 2+1):
                        rep.append(k)
                    for k in range(midgap // 2 + 1, 0, -1):
                        rep.append(k)
            if right<len(S):
                rep.append(0)
                left = right
                right = left + 1
        # after
        for k in range(1,right-left):
            rep.append(k)
        return rep

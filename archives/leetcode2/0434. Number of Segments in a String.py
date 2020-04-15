class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split(' ')
        cnt=0
        for ss in s:
            if ss:
                cnt+=1
        return cnt

class Solution:
    def rangeBitwiseAnd(self, m: 'int', n: 'int') -> 'int':
        cnt=0
        while m!=n:
            m=m>>1
            n=n>>1
            cnt+=1
        return m<<cnt

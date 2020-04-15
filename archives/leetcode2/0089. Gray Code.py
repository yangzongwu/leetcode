class Solution:
    def grayCode(self, n: 'int') -> 'List[int]':
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        dp=['0','1']
        while n>1:
            dp=['0'+x for x in dp]+['1'+x for x in dp[::-1]]
            n-=1
        rep=[int(x,2) for x in dp]
        return rep

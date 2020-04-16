class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        '''
        00000000000000 0
        00000000000001 1-----          2**1-1
        00000000000010 1  0
        00000000000011 2- 1---           2**2-1
        00000000000100 1    0
        00000000000101 2    1
        00000000000110 2    1
        00000000000111 3--- 2-          2**3-1
        00000000001000 1       0
        00000000001001 2       1
        00000000001010 2       1
        00000000001011 3       2
        00000000001100 2       1
        00000000001101 3       2
        00000000001110 3       2
        00000000001111 4----   3       2**4-1
        '''
        if num==0:
            return [0]
        if num==1:
            return [0,1]
        dp=[0,1]
        n=0
        while 2**n<num:
            n+=1
        for _ in range(n):
            dp=dp+[x+1 for x in dp]
        return dp[:num+1]
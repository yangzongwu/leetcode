class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        setj=set()
        for jj in J:
            setj.add(jj)
        
        cnt=0
        for ss in S:
            if ss in setj:
                cnt+=1
        return cnt

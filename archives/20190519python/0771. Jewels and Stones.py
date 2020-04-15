class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set=set()
        for j in J:
            J_set.add(j)
        cnt=0
        for s in S:
            if s in J_set:
                cnt+=1
        return cnt

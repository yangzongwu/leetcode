class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rep=[]
        for cur in ops:
            if cur=='C':
                rep.pop()
            elif cur=='D':
                rep.append(rep[-1]*2)
            elif cur=='+':
                rep.append(rep[-1]+rep[-2])
            else:
                rep.append(int(cur))
        return sum(rep)

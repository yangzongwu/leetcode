class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        rep=[]
        cur=0
        for num in A:
            cur=cur*2+int(num)
            if cur%5==0:
                rep.append(True)
            else:
                rep.append(False)
        return rep

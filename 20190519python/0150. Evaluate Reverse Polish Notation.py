class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rep=[]
        for token in tokens:
            if token not in "+-/*":
                rep.append(int(token))
            else:
                SN=rep.pop()
                FN=rep.pop()
                if token=='+':
                    rep.append(SN+FN)
                elif token=='-':
                    rep.append(FN-SN)
                elif token=='/':
                    if FN%SN==0 or FN/SN>0:
                        rep.append(FN//SN)
                    else:
                        rep.append(FN//SN+1)
                else:
                    rep.append(FN*SN)
        return rep[-1]

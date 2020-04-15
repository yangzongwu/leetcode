class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictdigits={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        rep=[]
        for s in digits:
            if not rep:
                for ss in dictdigits[s]:
                    rep.append(ss)
            else:
                tmp=[]
                for s1 in rep:
                    for s2 in dictdigits[s]:
                        tmp.append(s1+s2)
                rep=tmp
        return rep
                    

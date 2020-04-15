class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_letter={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                    '7':'pqrs','8':'tuv','9':'wxyz'}
        rep=[]
        for digit in digits:
            cur=[]
            if not rep:
                for ss in dict_letter[digit]:
                    cur.append(ss)
            else:
                for s1 in rep:
                    for s2 in dict_letter[digit]:
                        cur.append(s1+s2)
            rep=cur
        return rep

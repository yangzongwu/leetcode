'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        rep = ['(']
        repflag = [1]
        repflag2 = [1]
        lenrep=len(rep)

        for k in range(99999999999999):
            if k==len(repflag2):
                break
            while repflag2[k] < n:
                if repflag[k] == 0:
                    rep[k] += '('
                    repflag[k] += 1
                    repflag2[k] += 1
                else:
                    rep.append(rep[k] + ')')
                    repflag.append(repflag[k] - 1)
                    repflag2.append(repflag2[k])
                    rep[k] += '('
                    repflag[k] += 1
                    repflag2[k] += 1
                    lenrep+=1
            if repflag2[k] == n:
                while repflag[k] > 0:
                    rep[k] += ')'
                    repflag[k] -= 1
        return rep

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
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        if n==1:
            return ['()']
        
        res=['(']
        cur=[n-1]
        cnt=[1]

        rep=[]

        while res:
            if cur[-1]==0:
                rep.append(res.pop()+')'*cnt.pop())
                cur.pop()
            else:
                cur_s=res.pop()
                cur_count=cur.pop()
                cur_unfinish=cnt.pop()
                if cur_unfinish==0:
                    res.append(cur_s+'(')
                    cnt.append(cur_unfinish+1)
                    cur.append(cur_count-1)
                else:
                    res.append(cur_s+'(')
                    cnt.append(cur_unfinish+1)
                    cur.append(cur_count-1)
                    res.append(cur_s+')')
                    cnt.append(cur_unfinish-1)
                    cur.append(cur_count)
        return rep
                
        

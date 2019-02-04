class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return 0
        res=['(']
        resn=[1]
        resk=[1]
        rep=set()
        while res:
            cur_res=res.pop()
            cur_resn=resn.pop()
            cur_resk=resk.pop()
            if cur_resn==n:
                cur_res+=')'*cur_resk
                rep.add(cur_res)
            else:
                if cur_resk>0:
                    res.append(cur_res+')')
                    resk.append(cur_resk-1)
                    resn.append(cur_resn)     
                res.append(cur_res+'(')
                resk.append(cur_resk+1)
                resn.append(cur_resn+1)
               
        return list(rep)

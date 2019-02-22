class Solution:
    def reverseOnlyLetters(self, S: 'str') -> 'str':
        rep=[]
        res=''
        for ss in S:
            rep.append(ss)
            if ss in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                res=ss+res
        
        cur=0
        for k in range(len(rep)):
            if rep[k] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                rep[k]=res[cur]
                cur+=1
        return ''.join(rep)

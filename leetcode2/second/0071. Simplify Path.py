class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        while '/./' in path:
            path=path.replace('/./','//')
        while '//' in path:
            path=path.replace('//','/')
        path=path.split('/')[::-1]
        rep=[]
        cnt=0
        for s in path:
            if s=='..':
                cnt+=1
            elif s!='':
                if cnt>0:
                    cnt-=1
                else:
                    rep.append(s)
        if not rep:
            return '/'
        if rep[0]=='.':
            rep=rep[1:]
        if not rep:
            return '/'
        
        res=''
        for s in rep[::-1]:
            res=res+'/'+s
        
        return res

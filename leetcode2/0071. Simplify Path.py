class Solution:
    def simplifyPath(self, path: 'str') -> 'str':
        while '/./' in path:
            path=path.replace('/./','//')
        while '//' in path:
            path=path.replace('//','/')
        if path[-2:]=='/.':
            path=path[:-1]
        path=path.split('/')[::-1]
        rep=''
        cnt=0
        for s in path:
            if s:
                if s=='..':
                    cnt+=1
                else:
                    if cnt>0:
                        cnt-=1
                    else:
                        rep='/'+s+rep
        if not rep:
            return '/'
        return rep
        
            
        

class Solution:
    def simplifyPath(self, path: str) -> str:
        while '//' in path:
            path=path.replace('//','/')
        
        path_list=path.split('/')
        rep=[]
        for ss in path_list:
            if ss=='..':
                if rep:
                    rep.pop()
            elif ss and ss!='.':
                rep.append(ss)
        
        if not rep:
            return '/'
        
        result=""
        for ss in rep:
            result+='/'+ss
        return result
        

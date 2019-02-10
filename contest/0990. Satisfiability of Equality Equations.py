class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        rep=[]
        for equation in equations:
            if equation[1]=='=':
                flag=0
                for k in range(len(rep)):
                    if equation[0] in rep[k]:
                        flag=1
                        if equation[3] in rep[k]:
                            continue
                        else:
                            rep[k].add(equation[3])
                        break
                    elif equation[3] in rep[k]:
                        flag=1
                        rep[k].add(equation[0])
                        break
                if flag==1:
                    continue
                tmp=set(equation[0])
                tmp.add(equation[3])
                rep.append(tmp)
                        
        for equation in equations:
            if equation[1]=='!':
                if equation[0]==equation[3]:
                    return False
                for k in range(len(rep)):
                    if equation[0] in rep[k]:
                        if equation[3] in rep[k]:
                            return False
        return True
                              
                              
                
                                                 

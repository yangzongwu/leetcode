class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        if len(preorder)==1 and preorder[0]=='#':
            return True
        rep=[]
        preorder_list=preorder.split(',')
        for k in range(len(preorder_list)):
            if preorder_list[k]!='#':
                rep.append(preorder_list[k])
            else:
                if not rep:
                    return False
                elif rep[-1]!='#':
                    rep.append('#')
                else:
                    while len(rep)>1 and rep[-1]=='#':
                        rep.pop()
                        rep.pop()
                    if not rep:
                        if k==len(preorder_list)-1:
                            return True
                        return False
                    rep.append('#')

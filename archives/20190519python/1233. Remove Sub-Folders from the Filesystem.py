class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        rep=set()
        folder.sort(key=lambda x:len(x))
        for fold in folder:
            if fold in rep:
                continue
            cur=fold.split('/')
            flag=False
            for k in range(len(cur)-1,-1,-1):
                cur_path='/'.join(cur[:k])
                if cur_path in rep:
                    flag=True
                    continue
            if flag==True:
                continue
            rep.add(fold)
        return list(rep)

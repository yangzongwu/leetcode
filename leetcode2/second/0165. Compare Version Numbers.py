class Solution:
    def compareVersion(self, version1: 'str', version2: 'str') -> 'int':
        version1=version1.split('.')
        version2=version2.split('.')
        rep1,rep2=[],[]
        for version in version1:
            rep1.append(int(version))
        for version in version2:
            rep2.append(int(version))
        while rep1 and rep1[-1]==0:
            rep1=rep1[:-1]
        while rep2 and rep2[-1]==0:
            rep2=rep2[:-1]
            
        k=0
        while k<len(rep1):
            if k==len(rep2):
                return 1
            if rep1[k]>rep2[k]:
                return 1
            elif rep1[k]<rep2[k]:
                return -1
            else:
                k+=1
        if k==len(rep2):
            return 0
        else:
            return -1

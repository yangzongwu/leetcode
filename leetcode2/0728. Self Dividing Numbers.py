class Solution:
    def selfDividingNumbers(self, left: 'int', right: 'int') -> 'List[int]':
        rep=[]
        for n in range(left,right+1):
            if self.subselfDividingNumber(n):
                rep.append(n)
        return rep
    
    def subselfDividingNumber(self,n):
        if n<=0:
            return False
        elif n<10:
            return True
        else:
            s=str(n)
            if '0' in s:
                return False
            for ss in s:
                if n%int(str(ss))!=0:
                    return False
            return True

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a,b=b,a
        b=list(b[::-1])
        a=list(a[::-1])
        rep=""
        target='0'
        for i in range(len(b)):
            if a[i]=='1' and b[i]=='1' and target=='1':
                a[i],target='1','1'
            elif a[i]=='1' and b[i]=='0' and target=='1':
                a[i],target='0','1'
            elif a[i]=='1' and b[i]=='1' and target=='0':
                a[i],target='0','1'
            elif a[i]=='1' and b[i]=='0' and target=='0':
                a[i],target='1','0'
            elif a[i]=='0' and b[i]=='0' and target=='0':
                a[i],target='0','0'
            elif a[i]=='0' and b[i]=='1' and target=='0':
                a[i],target='1','0'
            elif a[i]=='0' and b[i]=='1' and target=='1':
                a[i],target='0','1'
            elif a[i]=='0' and b[i]=='0' and target=='1':
                a[i],target='1','0'
        if target=='1':
            for i in range(len(b),len(a)):
                if target=='0':
                    break
                if a[i]=='1' and target=='1':
                    a[i],target='0','1'
                elif a[i]=='0' and target=='1':
                    a[i],target='1','0'
        if target=='1':
            a.append('1')
        for s in a[::-1]:
            rep+=s
        return rep

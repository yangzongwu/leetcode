class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        lista=['a']*A
        listb=['b']*B
        if A<B:
            return self.substrWithout3a3b(B,A,listb,lista)
        else:
            return self.substrWithout3a3b(A,B,lista,listb)
    
    
    def substrWithout3a3b(self,A,B,lista,listb):
        rep=''
        if A<=2:
            rep=rep.join(lista)
            for ss in listb:
                rep+=ss
            return rep
        else:
            K=B-(A)//2
            while K>0 and len(lista)>=2 and len(listb)>=2:
                str1=lista.pop()
                str2=lista.pop()
                str3=listb.pop()
                str4=listb.pop()
                rep+=str1+str2+str3+str4
                K=K-1
            while lista and listb and len(lista)>=2 and len(listb)>=1:
                str1=lista.pop()
                str2=lista.pop()
                str3=listb.pop()
                rep+=str1+str2+str3
            if lista:
                for ss in lista:
                    rep+=ss
            if listb:
                for ss in listb:
                    rep+=ss
            return rep

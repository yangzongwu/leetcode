class Solution:
    def computeArea(self, A: 'int', B: 'int', C: 'int', D: 'int', E: 'int', F: 'int', G: 'int', H: 'int') -> 'int':
        #Aleft Bdown Cright Dup 
        #Eleft Fdown Gright Hup
        tmparea=0
        if (min(D,H)-max(B,F))>0 and (min(C,G)-max(A,E))>0: 
            tmparea=(min(D,H)-max(B,F))*(min(C,G)-max(A,E))
        totalarea=(C-A)*(D-B)+(G-E)*(H-F)
        return totalarea-tmparea

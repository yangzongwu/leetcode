class Solution:
    def isValid(self, S: str) -> bool:
        if S[0]!='a':
            return False
        if len(S)%3!=0:
            return False
        while 'abc' in S:
            S=S.replace('abc','')
        if not S:
            return True
        return False
        

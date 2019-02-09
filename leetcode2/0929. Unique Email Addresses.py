class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        k=0
        while k<len(emails):
            emails[k]=self.reWriteEmail(emails[k])
            k+=1
        cnt=0
        for _ in list(set(emails)):
            cnt+=1
        return cnt
    
    def reWriteEmail(self,email):
        rep=email.split('@')
        rep[0]=rep[0].replace('.','')
        k=0
        while k<len(rep[0]):
            if rep[0][k]!='+':
                k+=1
            else:
                break
        rep[0]=rep[0][:k]
        return rep[0]+'@'+rep[1]

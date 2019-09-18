class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set=set()
        for email in emails:
            cur_email=self.getEmail(email)
            email_set.add(cur_email)
        return len(email_set)
    
    def getEmail(self,email):
        cur=email.split('@')
        tmp=cur[0].replace('.','')
        k=0
        while k<len(tmp) and tmp[k]!='+':
            k+=1
        if k==len(tmp):
            return tmp+'@'+cur[1]
        return tmp[:k]+'@'+cur[1]

class Solution:
    def checkRecord(self, s: str) -> bool:
        flag=0
        k=0
        while k in range(len(s)):
            if s[k]=='A':
                if flag==1:
                    return False
                flag=1
            elif s[k]=='L' and k<len(s)-2:
                if s[k+1]==s[k+2]=='L':
                    return False
            k+=1
        return True

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        rep=1
        for k in range(1,len(text)-1):
            if text[k]!=text[k-1]:
                i=0
                cnt=1
                target=text[k-1]
                left=k-1-1
                right=k+1
                while left>=0 and text[left]==target:
                    left-=1
                    cnt+=1
                while right<len(text) and text[right]==target:
                    right+=1
                    cnt+=1
                if left>0:
                    if target in text[:left] or target in text[right:]:
                        rep=max(rep,cnt+1)
                    else:
                        rep=max(rep,cnt)
                else:
                    if  target in text[right:]:
                        rep=max(rep,cnt+1)
                    else:
                        rep=max(rep,cnt)
        target=text[0]            
        cnt=1
        for k in range(1,len(text)):
            if text[k]==target:
                cnt+=1
            else:
                rep=max(rep,cnt)
                cnt=1
                target=text[k]
        rep=max(rep,cnt)
        return rep

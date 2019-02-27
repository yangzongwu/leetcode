class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        if not s:
            return []
        
        dp=[[[s[0]]]]
        for k in range(1,len(s)):
            left=0
            tmp=[]
            while left<=k:
                if left==0:
                    if s[:k+1]==s[:k+1][::-1]:
                        tmp.append([s[:k+1]])
                else:
                    if s[left:k+1]==s[left:k+1][::-1]:
                        for cur in dp[left-1]:
                            tmp.append(cur+[s[left:k+1]])
                left+=1
            dp.append(tmp)
        return dp[-1]

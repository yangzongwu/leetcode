class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        dp=[]
        wordDict=set(wordDict)
        for k in range(1,len(s)+1):
            if s[:k] in wordDict:
                dp.append(True)
            else:
                flag=False
                for j in range(0,k-1):
                    if dp[j] and s[j+1:k] in wordDict:
                        flag=True
                        continue
                dp.append(flag)
        return dp[-1]
                        

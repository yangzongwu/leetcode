class Solution:
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        wordDict=set(wordDict)
        dp=[False]*len(s)
        for k in range(len(s)):
            print(dp)
            if s[:k+1] in wordDict:
                dp[k]=True
            else:
                j=1
                while j<k+1:
                    if dp[j-1]==True and s[j:k+1] in wordDict:
                        dp[k]=True
                        break
                    else:
                        j+=1
        return dp[-1]

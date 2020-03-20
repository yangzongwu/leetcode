'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0]=='0':
            return 0
        dp=[1,1]
        for k in range(1,len(s)):
            if s[k-1]=='0':
                if s[k]=='0':
                    return 0
                dp.append(dp[-1])
            elif s[k-1]=='1':
                if s[k]=='0':
                    dp.append(dp[-2])
                else:
                    dp.append(dp[-1]+dp[-2])
            elif s[k-1]=='2':
                if s[k]=='0':
                    dp.append(dp[-2])
                elif s[k] in '123456':
                    dp.append(dp[-1]+dp[-2])
                else:
                    dp.append(dp[-1])
            else:
                if s[k]=='0':
                    return 0
                dp.append(dp[-1])
        return dp[-1]

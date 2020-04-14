'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2)>len(str1):
            str1,str2=str2,str1
        for i in range(len(str2),0,-1):
            cur=str2[:i]
            if len(str1)%i==0 and len(str2)%i==0 and cur*(len(str1)//i)==str1 and cur*(len(str2)//i)==str2:
                return cur
        return ""

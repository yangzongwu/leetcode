'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

'''
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        strs="qwertyuiopasdfghjklzxcvbnm"
        strs+=strs.upper()
        list_S=[x for x in S]
        l=0
        r=len(list_S)-1
        while l<r:
            while l<r and list_S[l] not in strs:
                l+=1
            while r>l and list_S[r] not in strs:
                r-=1
            if l>=r:
                break
            list_S[l],list_S[r]=list_S[r],list_S[l]
            l+=1
            r-=1
        return ''.join(list_S)


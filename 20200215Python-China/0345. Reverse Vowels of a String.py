'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list=[]
        v_list=[]
        for k in range(len(s)):
            s_list.append(s[k])
            if s[k] in 'aeoiuAEIOU':
                v_list.append(k)
        l,r=0,len(v_list)-1
        while l<r:
            s_list[v_list[l]],s_list[v_list[r]]=s_list[v_list[r]],s_list[v_list[l]]
            l+=1
            r-=1
        return ''.join(s_list)

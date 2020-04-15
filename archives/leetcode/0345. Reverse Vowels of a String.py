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
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=''
        lists=[]
        for x in s:
            lists.append(x)
            if x in 'aoiueAOIUE':
                ss+=x
        ss=ss[::-1]
        
        i=0
        j=0
        while i<len(lists):
            if lists[i] in 'aoiueAOIUE':
                lists[i]=ss[j]
                j+=1
            i+=1
            
        s=''
        for ss in lists:
            s+=ss
        return s

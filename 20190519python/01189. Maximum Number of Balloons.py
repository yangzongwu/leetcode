'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon
        dict_text={}
        for t in text:
            if t not in dict_text:
                dict_text[t]=1
            else:
                dict_text[t]+=1
        
        for s in 'balon':
            if s not in dict_text:
                return 0
            
        return min(dict_text['a'],dict_text['b'],dict_text['n'],dict_text['l']//2,dict_text['o']//2)
        

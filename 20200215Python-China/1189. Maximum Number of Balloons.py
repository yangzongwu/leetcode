'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

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
text consists of lower case English letters only.

'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict_text = {}
        for c in text:
            if c not in dict_text:
                dict_text[c] = 1
            else:
                dict_text[c] += 1

        cnt = len(text)
        for s in 'banlo':
            if s not in dict_text:
                return 0
            if s in 'ban':
                cnt = min(cnt, dict_text[s])
            else:
                cnt = min(cnt, dict_text[s] // 2)

        return cnt
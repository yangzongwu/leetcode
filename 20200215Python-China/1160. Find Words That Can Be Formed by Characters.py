"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        for s in chars:
            if s not in chars_dict:
                chars_dict[s] = 1
            else:
                chars_dict[s] += 1

        rep = 0
        for word in words:
            if self.canBeFormed(word, chars_dict):
                rep += len(word)
        return rep

    def canBeFormed(self, word, dict_s):
        cur = {}
        for s in word:
            if s not in dict_s:
                return False
            if s not in cur:
                cur[s] = 1
            else:
                if cur[s] == dict_s[s]:
                    return False
                cur[s] += 1
        return True
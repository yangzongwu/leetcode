'''
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

'''


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        rep = []
        len_singleword = len(words[0])
        len_totalwords = len(words) * len_singleword
        dict_words = {}
        for word in words:
            if word not in dict_words:
                dict_words[word] = 1
            else:
                dict_words[word] += 1
        s_len = len(s)
        if s_len < len_totalwords:
            return rep
        for k in range(0, len(s) - len_totalwords + 1):
            if self.matchstring(dict_words, s[k:k + len_totalwords], len_singleword):
                rep.append(k)
        return rep

    def matchstring(self, dictwords, s, k):
        tmp_dict = {}
        for m in range(0, len(s) - k + 1, k):
            if s[m:m + k] not in tmp_dict:
                tmp_dict[s[m:m + k]] = 1
            else:
                tmp_dict[s[m:m + k]] += 1
        for key in tmp_dict:
            if key not in dictwords:
                return False
            if tmp_dict[key] != dictwords[key]:
                return False
        for key in dictwords:
            if key not in tmp_dict:
                return False
        return True

if __name__=='__main__':
    Test=Solution()
    print(Test.findSubstring("barfoothefoobarman",["foo","bar"]))

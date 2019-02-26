class Solution:
    def longestSubstring(self, s: 'str', k: 'int') -> 'int':
        if len(s)<k:
            return 0
        for ss in set(s):
            if s.count(ss)<k:
                return max(self.longestSubstring(str1,k) for str1 in s.split(ss))
        return len(s)

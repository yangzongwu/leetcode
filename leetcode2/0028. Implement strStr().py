class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        len_needle=len(needle)
        for k in range(len(haystack)-len_needle+1):
            if haystack[k:k+len_needle]==needle:
                return k
        return -1

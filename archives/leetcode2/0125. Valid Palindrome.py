class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rep=''
        for ss in s.lower():
            if ss in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                rep+=ss
        return rep==rep[::-1]

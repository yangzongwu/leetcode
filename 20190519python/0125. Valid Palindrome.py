class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower();
        rep=""
        for ss in s:
            if ss in "qwertyuiopasdfghjklzxcvbnm1234567890":
                rep+=ss
        return rep==rep[::-1]

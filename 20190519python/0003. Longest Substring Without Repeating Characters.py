class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_list=set()
        if not s:
            return 0
        left=0
        right=0
        rep=0
        while right<len(s):
            while right<len(s) and s[right] not in cur_list:
                cur_list.add(s[right])
                right+=1
            rep=max(rep,right-left)
            if right!=len(s):
                while s[left]!=s[right]:
                    cur_list.remove(s[left])
                    left+=1
                left+=1
                right+=1
        return rep

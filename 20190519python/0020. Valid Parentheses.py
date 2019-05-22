class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while "()" in s or "[]" in s or "{}" in s:
            if "()" in s:
                s=s.replace("()","")
            elif "[]" in s:
                s=s.replace("[]","")
            else:
                s=s.replace("{}","")
        return len(s)==0
#=============================================================
class Solution:
    def isValid(self, s: str) -> bool:
        rep=[]
        for ss in s:
            if ss in  "{[(":
                rep.append(ss)
            elif len(rep)==0:
                return False
            elif ss=="]" and rep[-1]!="[":
                return False
            elif ss=="}" and rep[-1]!="{":
                return False
            elif ss==")" and rep[-1]!="(":
                return False
            else:
                rep.pop()
        return len(rep)==0

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_s={')':'(',']':'[','}':'{'}
        if not s:
            return True
        stack_s=[]
        for ss in s:
            if not stack_s:
                if ss in dict_s:
                    return False
                else:
                    stack_s.append(ss)
            else:
                if ss not in dict_s:
                    stack_s.append(ss)
                else:
                    if stack_s[-1]!=dict_s[ss]:
                        return False
                    else:
                        stack_s.pop()
        if not stack_s:
            return True
        else:
            return False

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str_s=self.afterBackspace(S)
        str_t=self.afterBackspace(T)
        return str_s==str_t

    def afterBackspace(self,s):
        stack=[]
        for ss in s:
            if ss == "#":
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(ss)
        return str(stack)

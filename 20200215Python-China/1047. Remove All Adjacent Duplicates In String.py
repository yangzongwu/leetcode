class Solution:
    def removeDuplicates(self, S: str) -> str:
        s_stack=[]
        for ss in S:
            if not s_stack:
                s_stack.append(ss)
            else:
                if s_stack[-1]==ss:
                    s_stack.pop()
                else:
                    s_stack.append(ss)

        rep="".join(ss for ss in s_stack)
        return rep

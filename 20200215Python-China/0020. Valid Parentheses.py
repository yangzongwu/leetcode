class Solution:
    def isValid(self, s: str) -> bool:
        s_stack=[]
        for ss in s:
            if ss in "{([":
                s_stack.append(ss)
            else:
                if not s_stack:
                    return False
                if ss==']' and s_stack[-1]=="[":
                    s_stack.pop()
                elif ss==']' and s_stack[-1]=="[":
                    s_stack.pop()
                elif ss=='}' and s_stack[-1]=="{":
                    s_stack.pop()
                elif ss==')' and s_stack[-1]=="(":
                    s_stack.pop()
                else:
                    return False
        return len(s_stack)==0

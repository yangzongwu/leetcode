class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return int(s)
        
        flag=False
        s_stack=[]
        
        l=0
        r=1
        while r<len(s):
            while r<len(s) and s[r] not in '+-*/':
                r+=1
            if r==len(s):
                if flag==True:
                    flag1=s_stack.pop()
                    FN=int(s_stack.pop())
                    SN=int(s[l:r])
                    if flag1=='*':
                        s_stack.append(FN*SN)
                    else:
                        s_stack.append(FN//SN)
                    flag=False
                else:
                    s_stack.append(int(s[l:r]))
                break
            else:#r<len(s):
                if flag==True:
                    flag1=s_stack.pop()
                    FN=int(s_stack.pop())
                    SN=int(s[l:r])
                    if flag1=='*':
                        s_stack.append(FN*SN)
                    else:
                        s_stack.append(FN//SN)
                    flag=False
                else:
                    s_stack.append(int(s[l:r]))
                if s[r] in '*/':
                    flag=True
                s_stack.append(s[r])
                r+=1
                l=r
            
        if not s_stack:
            return 0
        rep=s_stack.pop(0)
        while s_stack:
            flag2=s_stack.pop(0)
            if flag2=='+':
                rep+=s_stack.pop(0)
            else:
                rep-=s_stack.pop(0)
        return rep

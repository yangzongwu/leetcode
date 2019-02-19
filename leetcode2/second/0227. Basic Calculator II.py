class Solution:
    def calculate(self, s: 'str') -> 'int':
        s=s.replace(' ','')
        if not s:
            return 0
        s_stack=[]
        k=0
        while k<len(s):
            if s[k] in '+-*/':
                s_stack.append(s[k])
                k+=1
            else:# s[k] in '1234567890':
                j=0
                while k+j<len(s) and s[k+j] in '1234567890':
                    j+=1
                s_stack.append(s[k:k+j])
                k+=j
                
        tmp_stack=[]
        k=0
        while k<len(s_stack):
            if s_stack[k] not in '*/':
                tmp_stack.append(s_stack[k])
                k+=1
            else:
                
                prev=int(tmp_stack.pop())
                cur=int(s_stack[k+1])
                if s_stack[k]=='*':
                    tmp_stack.append(prev*cur)
                else:
                    tmp_stack.append(prev//cur)
                k+=2
        
        rep=int(tmp_stack[0])
        k=1
        while k<len(tmp_stack):
            if tmp_stack[k]=='+':
                rep+=int(tmp_stack[k+1])
            else:
                rep-=int(tmp_stack[k+1])
            k+=2
        return rep

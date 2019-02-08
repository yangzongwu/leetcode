class Solution:
    def evalRPN(self, tokens: 'List[str]') -> 'int':
        stack_tokens=[]
        for token in tokens:
            if token not in '+-/*':
                stack_tokens.append(token)
            else:
                second=int(stack_tokens.pop())
                first=int(stack_tokens.pop())
                if token=='+':
                    stack_tokens.append(str(first+second))
                elif token=='-':
                    stack_tokens.append(str(first-second))
                elif token=='*':
                    stack_tokens.append(str(first*second))
                else:# token=='/':
                    if first*second>=0 or (first*second<0 and first%second==0):
                        stack_tokens.append(str(first//second))
                    else:
                        stack_tokens.append(str(first//second+1))
        return int(stack_tokens[-1])

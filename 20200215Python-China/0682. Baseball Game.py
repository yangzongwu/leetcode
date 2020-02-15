class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ops_stack=[]
        for op in ops:
            if op=='C':
                ops_stack.pop()
            elif op=='D':
                ops_stack.append(ops_stack[-1]*2)
            elif op=='+':
                ops_stack.append(ops_stack[-1]+ops_stack[-2])
            else:
                ops_stack.append(int(op))
        return sum(ops_stack)

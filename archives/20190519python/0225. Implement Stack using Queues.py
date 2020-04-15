class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=[]
    
    
    def qpush(self,q,x):
        q.insert(0,x)
        return
    def qpop(self,q):
        return q.pop()
    def qpeek(self,q):
        return q[-1]
    
    
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.qpush(self.q,x)
            

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        tmp=[]
        while len(self.q)>1:
            self.qpush(tmp,self.qpop(self.q))
        rep=self.qpop(self.q)
        while tmp:
            self.qpush(self.q,self.qpop(tmp))
        return rep
        
    def top(self) -> int:
        """
        Get the top element.
        """
        tmp=[]
        while len(self.q)>1:
            self.qpush(tmp,self.qpop(self.q))
        rep=self.qpeek(self.q)
        self.qpush(tmp,self.qpop(self.q))
        while tmp:
            self.qpush(self.q,self.qpop(tmp))
        return rep

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q==[]
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=[]
        
    def qpeek(self,q):
        return q[0]
    def qpop(self,q):
        return q.pop(0)
    def qpush(self,q,x):
        q.insert(0,x)
        return
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.q1:
            self.qpush(self.q1,x)
        else:
            q2=[]
            while self.q1:
                self.qpush(q2,self.qpop(self.q1))
            self.qpush(self.q1,x)
            while q2:
                self.qpush(self.q1,self.qpop(q2))
        print(self.q1)
            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.qpop(self.q1)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.qpeek(self.q1)
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.q1==[]
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

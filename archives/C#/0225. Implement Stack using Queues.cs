public class MyStack {

    Queue<int> myStack= new Queue<int>();
    Queue<int> tmpQueue= new Queue<int>();
    /** Initialize your data structure here. */
    public MyStack() {
        
    }
    
    /** Push element x onto stack. */
    public void Push(int x) {
        myStack.Enqueue(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int Pop() {
        while(myStack.Count>1){
            int x =myStack.Dequeue();
            tmpQueue.Enqueue(x);
        }
        int result=myStack.Dequeue();
        while(tmpQueue.Count>0){
            int x =tmpQueue.Dequeue();
            myStack.Enqueue(x);
        }
        return result;
    }
    
    /** Get the top element. */
    public int Top() {
        while(myStack.Count>1){
            int x =myStack.Dequeue();
            tmpQueue.Enqueue(x);
        }
        int result=myStack.Dequeue();
        tmpQueue.Enqueue(result);
        while(tmpQueue.Count>0){
            int x =tmpQueue.Dequeue();
            myStack.Enqueue(x);
        }
        return result;
    }
    
    /** Returns whether the stack is empty. */
    public bool Empty() {
        return myStack.Count==0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */

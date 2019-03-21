public class MyQueue {

    Stack<int> myQueue= new Stack<int>();
    Stack<int> tmpQueue= new Stack<int>();
    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void Push(int x) {
        if(myQueue.Count()==0){
            myQueue.Push(x);
        }
        else{
            while(myQueue.Count()!=0){
                int i=myQueue.Pop();
                tmpQueue.Push(i);
            }
            myQueue.Push(x);
            while(tmpQueue.Count()!=0){
                int i=tmpQueue.Pop();
                myQueue.Push(i);
            }            
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int Pop() {
        return myQueue.Pop();
    }
    
    /** Get the front element. */
    public int Peek() {
        return myQueue.Peek();
    }
    
    /** Returns whether the queue is empty. */
    public bool Empty() {
        return myQueue.Count()==0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */

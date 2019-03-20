public class MinStack {
    
    Stack<int> stackS=new Stack<int>();
    Stack<int> minStack=new Stack<int>();
    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void Push(int x) {
        stackS.Push(x);
        if (minStack.Count==0 || minStack.Peek()>=x){
            minStack.Push(x);
        }
    }
    
    public void Pop() {
        int tmp=stackS.Pop();
        if(tmp==minStack.Peek()){
            minStack.Pop();
        }
    }
    
    public int Top() {
        return stackS.Peek();
    }
    
    public int GetMin() {
         return minStack.Peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */

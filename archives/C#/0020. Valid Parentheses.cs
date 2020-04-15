public class Solution {
    public bool IsValid(string s) {
        Stack<char> sStack=new Stack<char>();
        foreach(char ss in s){
            if (sStack.Count==0){
                sStack.Push(ss);
            }
            else{
                if (ss==')' && sStack.Peek()=='('){
                    sStack.Pop();
                }
                else if(ss==']' && sStack.Peek()=='['){
                    sStack.Pop();
                }else if(ss=='}' && sStack.Peek()=='{'){
                    sStack.Pop();
                }
                else{
                    sStack.Push(ss);
                }
            }
        }
        return sStack.Count==0;
    }
}

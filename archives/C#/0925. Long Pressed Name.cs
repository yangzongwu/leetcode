public class Solution {
    public bool IsLongPressedName(string name, string typed) {
        Stack<char> nameStack=new Stack<char>();
        Stack<int> nameStackCnt=new Stack<int>();
        Stack<char> typedStack=new Stack<char>();
        Stack<int> typedStackCnt=new Stack<int>();
        foreach(char c in name){
            if(nameStack.Count()==0){
                nameStack.Push(c);
                nameStackCnt.Push(1);
            }
            else if(nameStack.Peek()!=c){
                nameStack.Push(c);
                nameStackCnt.Push(1);
            }
            else{
                nameStackCnt.Push(nameStackCnt.Pop()+1);
            }
        }
        

        
                
        foreach(char c in typed){
            if(typedStack.Count()==0){
                typedStack.Push(c);
                typedStackCnt.Push(1);
            }
            else if(typedStack.Peek()!=c){
                typedStack.Push(c);
                typedStackCnt.Push(1);
            }else{
                typedStackCnt.Push(typedStackCnt.Pop()+1);
            }
        }
        if(nameStack.Count()!=typedStack.Count()){
            return false;
        }
        else{
            bool flag=true;
            while(nameStack.Count()!=0){
                var char1=nameStack.Pop();
                var char2=typedStack.Pop();
                var x=typedStackCnt.Pop();
                var y=nameStackCnt.Pop();
                //Console.WriteLine("{0},{1},{2},{3}",char1,char2,x,y);
                if (char1!=char2||x<y){
                    flag=false;
                    break;
                }
            }
            return flag;
        }
    }
}

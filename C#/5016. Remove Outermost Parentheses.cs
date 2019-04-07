public class Solution {
    public string RemoveOuterParentheses(string S) {
        if(S==""){
            return "";
        }
        Stack<char> sStack=new Stack<char>();
        string rep="";
        string tmp="";
        foreach(char c in S){
            if(sStack.Count()==0){
                sStack.Push(c);
            }
            else{
                if(sStack.Peek()=='(' && c=='('){
                    sStack.Push(c);
                    tmp+=c;
                }
                else if(sStack.Peek()=='(' && c==')'){
                    sStack.Pop();
                    if(sStack.Count()==0){
                        rep+=tmp;
                        tmp="";
                    }
                    else{
                        tmp+=c;
                    }
                }
            }
        }
        return rep;
    }
}

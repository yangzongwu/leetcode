public class Solution {
    public bool RepeatedSubstringPattern(string s) {
        bool flag=false;
        for(int i=1;i<s.Length;i++){
            if(s.Length%i==0 && IsRepeatedSubtring(s,s.Substring(0,i),i)){
                flag=true;
                break;
            }
        }
        return flag;
    }
    
    public bool IsRepeatedSubtring(string s,string str,int k){
        if(s.Length==0){
            return true;
        }
        if(s.Substring(0,k)!=str){
            return false;
        }
        return IsRepeatedSubtring(s.Substring(k),str,k);
    }
}

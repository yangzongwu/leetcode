public class Solution {
    public string CountAndSay(int n) {
        string rep="1";
        while(n>1){
            rep=CalCountAndSay(rep);
            n--;
        }
        return rep;
    }
    
    public string CalCountAndSay(string s){
        int left=0;
        int cnt=0;
        char target=s[0];
        string rep="";
        while (left<s.Length){
            if(s[left]==target){
                cnt++;
                left++;
            }
            else{
                rep=rep+cnt.ToString()+target;
                cnt=0;
                target=s[left];
            }
        }
        rep=rep+cnt.ToString()+target;
        return rep;
        
    }
}

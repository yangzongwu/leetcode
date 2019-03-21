public class Solution {
    public string ConvertToTitle(int n) {
        string s="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        string rep="";
        while (n>0){
            if(n%26!=0){
                int tmp=n%26;
                rep=s[tmp-1]+rep;
                n=n/26;
            }
            else{
                rep='Z'+rep;
                n=(n-1)/26;
            }
        }
        return rep;
    }
}

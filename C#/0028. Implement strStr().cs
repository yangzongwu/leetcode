public class Solution {
    public int StrStr(string haystack, string needle) {
        int loc=-1;
        for(int i=0;i<haystack.Length-needle.Length+1;i++){
            if(checkIsSame(haystack,needle,i)){
                loc=i;
                break;
            }
        }
        return loc;
    }
    
    public bool checkIsSame(string haystack, string needle,int k){
        bool flag=true;
        for(int i=0;i<needle.Length;i++){
            if(needle[i]!=haystack[i+k]){
                flag=false;
                break;
            }
        }
        return flag;
    }
}

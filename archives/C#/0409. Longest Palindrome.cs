public class Solution {
    public int LongestPalindrome(string s) {
        if(s.Length==0){
            return 0;
        }
        Dictionary<char,int> sDict=new Dictionary<char,int>();
        foreach(char c in s){
            if(!sDict.ContainsKey(c)){
                sDict[c]=1;
            }
            else{
                sDict[c]+=1;
            }
        }
        int rep=0;
        int tmp=0;
        foreach(int sDictValue in sDict.Values){
            rep+=(sDictValue/2)*2;
            tmp+=sDictValue%2;
        }
        return tmp>0?rep+1:rep;
    }
}

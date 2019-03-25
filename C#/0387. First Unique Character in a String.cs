public class Solution {
    public int FirstUniqChar(string s) {
        Dictionary<char,int> sDict=new Dictionary<char,int>();
        foreach(char c in s){
            if(!sDict.ContainsKey(c)){
                sDict[c]=1;
            }
            else{
                sDict[c]+=1;
            }
        }
        int loc=0;
        while(loc<s.Length){
            if(sDict[s[loc]]==1){
                break;
            }
            loc++;
        }
        return loc==s.Length?-1:loc;
    }
}

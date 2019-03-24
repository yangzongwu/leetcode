public class Solution {
    public char FindTheDifference(string s, string t) {
        Dictionary<char,int> tDict=new Dictionary<char,int>();
        foreach(char c in t){
            if(!tDict.ContainsKey(c)){
                tDict[c]=1;
            }
            else{
                tDict[c]+=1;
            }
        }
        foreach(char c in s){
            tDict[c]-=1;
        }
        char rep=new char();
        foreach(KeyValuePair<char,int> kvp in tDict){
            if (kvp.Value!=0){
                rep=kvp.Key;
            }
        }
        return rep;
        
    }
}

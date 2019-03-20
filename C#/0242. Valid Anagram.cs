public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length!=t.Length){
            return false;
        }
        IDictionary<char,int> cmpDict=new Dictionary<char,int>();
        foreach(char ss in s){
            if(!cmpDict.ContainsKey(ss)){
                cmpDict[ss]=1;
            }
            else{
                cmpDict[ss]+=1;
            }
        }
        bool rep=true;
        foreach(char ss in t){
            if(cmpDict.ContainsKey(ss)){
                cmpDict[ss]-=1;
            }
            else{
                rep=false;
                break;
            }
        }
        
        if(rep==false){return false;}
        foreach(char key in cmpDict.Keys){
            if(cmpDict[key]!=0){
                rep=false;
                break;
            }
        }
        return rep;
    }
}

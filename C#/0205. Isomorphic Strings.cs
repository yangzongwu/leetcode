public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if(s.Length!=t.Length){return false;}
        IDictionary<char,char> sDict=new Dictionary<char,char>();
        HashSet<char> tSet=new HashSet<char>();
        
        bool flag=true;
        for(int i=0;i<s.Length;i++){
            if(!sDict.ContainsKey(s[i]) && tSet.Contains(t[i])){
                flag=false;
                break;
            }
            else if (!sDict.ContainsKey(s[i]) && !tSet.Contains(t[i])){
                sDict.Add(s[i],t[i]);
                tSet.Add(t[i]);
            }
            else if (sDict.ContainsKey(s[i]) && sDict[s[i]]!=t[i]){
                flag=false;
                break;
            }
        }
        return flag;
    }
}

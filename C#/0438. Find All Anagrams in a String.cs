public class Solution {
    public IList<int> FindAnagrams(string s, string p) {
        IList<int> rep=new List<int>();
        if(s.Length<p.Length){
            return rep;
        }
        Dictionary<char,int> sDict=new Dictionary<char,int>();
        Dictionary<char,int> pDict=new Dictionary<char,int>();
        for(int i=0;i<p.Length;i++){
            pDict[p[i]]=!pDict.ContainsKey(p[i])?1:pDict[p[i]]+1;
            sDict[s[i]]=!sDict.ContainsKey(s[i])?1:sDict[s[i]]+1;
        }
        if(IsAnagram(sDict,pDict)){
                rep.Add(0);
        }
        for(int i=1;i<s.Length-p.Length+1;i++){
            sDict[s[i-1]]-=1;
            if(sDict[s[i-1]]==0){
                sDict.Remove(s[i-1]);
            }
            sDict[s[i+p.Length-1]]=!sDict.ContainsKey(s[i+p.Length-1])?1:(sDict[s[i+p.Length-1]]+1);
            if(IsAnagram(sDict,pDict)){
                rep.Add(i);
            }  
        }
        return rep; 
    }
    public bool IsAnagram(Dictionary<char,int> sDict,Dictionary<char,int> pDict){
        bool flag=true;
        foreach(KeyValuePair<char,int> kvp in sDict){
            if(!pDict.ContainsKey(kvp.Key) || pDict[kvp.Key]!=kvp.Value){
                flag=false;
                break;
            }
        }
        return flag;
    }
}

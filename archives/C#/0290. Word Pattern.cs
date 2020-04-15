public class Solution {
    public bool WordPattern(string pattern, string str) {
        string[] stringStr=str.Split(" ");
        if(pattern.Length!=stringStr.Length){
            return false;
        }
        Dictionary<char,string> dictCmp=new Dictionary<char,string>();
        HashSet<string> strSet=new HashSet<string>();
        bool flag=true;
        for(int i=0;i<pattern.Length;i++){
            if(!dictCmp.ContainsKey(pattern[i])){
                if (!strSet.Contains(stringStr[i])){
                    dictCmp[pattern[i]]=stringStr[i];
                    strSet.Add(stringStr[i]);
                }
                else{
                    flag=false;
                    break;
                }
            }
            else{
                if(dictCmp[pattern[i]]!=stringStr[i]){
                    flag=false;
                    break;
                }
            }
        }
        return flag;
    }
}

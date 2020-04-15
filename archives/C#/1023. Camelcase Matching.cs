public class Solution {
    public IList<bool> CamelMatch(string[] queries, string pattern) {
        IList<bool> rep=new List<bool>();
        List<string> patternList=new List<string>();
        patternList=CurString(pattern);
        
        for(int i=0;i<queries.Length;i++){
            if(CamelMatch(queries[i],patternList)==true){
                rep.Add(true);
            }
            else{
                rep.Add(false);
            }
        }
        return rep;
    }
    
    public bool CamelMatch(string str,List<string> patternList){
        List<string> strList=new List<string>();
        strList=CurString(str);
        if(strList.Count()!=patternList.Count()){
            return false;
        }
        for(int i=0;i<strList.Count();i++){
            if(PreSubString(strList[i],patternList[i])==false){
                return false;
            }
        }
        return true;
    }
    
    public bool PreSubString(string str1,string str2){
        if(str2.Length>str1.Length){
            return false;
        }
        int left=0;
        for(int i=0;i<str2.Length;i++){
            while(left<str1.Length && str2[i]!=str1[left]){
                left++;
            }
            if(left==str1.Length){
                return false;
            }
            else{
                left++;
            }
            
        }
        return true;
    }
    
    public List<string> CurString(string str){
        List<string> rep=new List<string>();
        string ss="";
        string stringUpper="QWERTYUIOPASDFGHJKLZXCVBNM";
        foreach(char c in str){
            if(stringUpper.Contains(c)){
                if(ss.Length>0){
                    if(stringUpper.Contains(ss[0])){
                        rep.Add(ss);
                    }
                }
                ss=""+c;
            }
            else{
                ss+=c;
            }
        }
        rep.Add(ss);
        return rep;
    }
}

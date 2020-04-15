public class Solution {
    public string[] FindWords(string[] words) {        
        List<string> rep=new List<string>();
        foreach(string word in words){
            if(AtOneLine(word)){
                rep.Add(word);
            }
        }
        return rep.ToArray();
    }
    
    public bool AtOneLine(string word){
        string str1="qwertyuiopQWERTYUIOP";
        string str2="asdfghjklASDFGHJKL";
        string str3="zxcvbnmZXCVBNM";
        if(word.Length==1){
            return true;
        }
        string target="";
        if(str1.Contains(word[0])){
            target=str1;
        }
        else if(str2.Contains(word[0])){
            target=str2;
        }
        else if(str3.Contains(word[0])){
            target=str3;
        }
        
        bool rep=true;
        for(int i=1;i<word.Length;i++){
            if(!target.Contains(word[i])){
                rep=false;
                break;
            }
        }
        return rep;
        
    }
}

public class Solution {
    public string ReverseWords(string s) {
        List<string> strList=new List<string>();
        int left=0;
        int cur=left;
        while(cur<s.Length){
            if(s[cur]==' ')
                cur++;
            else{
                left=cur;
                while(cur<s.Length && s[cur]!=' '){
                    cur++;
                }
                strList.Add(s.Substring(left,cur-left));
                left=cur;
                cur++;
            }
        }
        
        if(strList.Count()==0)
            return "";
        
        string str="";
        for(int i=strList.Count()-1;i>=0;i--){
            str+=" "+strList[i];
        }
        return str.Substring(1);
    }
}

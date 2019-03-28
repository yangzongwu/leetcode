public class Solution {
    public string LongestWord(string[] words) {
        Array.Sort(words,(x,y)=>x.Length.CompareTo(y.Length));
        if(words[0].Length!=1){
                return "";
        }
        
        string result="";
        HashSet<string> wordsSet=new HashSet<string>();
        for(int i=0;i<words.Count();i++){
            if(words[i].Length==1){
                wordsSet.Add(words[i]);
                if(result=="" || CompareString(result,words[i])){
                    result=words[i];
                }
            }
            else{
                string subWord=words[i].Substring(0,words[i].Length-1);
                if((words[i].Length-words[i-1].Length==0) && wordsSet.Contains(subWord)){
                    wordsSet.Add(words[i]);
                    if(words[i].Length>result.Length || CompareString(result,words[i])){
                        result=words[i];
                    }
                }
                else if((words[i].Length-words[i-1].Length==1) && wordsSet.Contains(subWord)){
                    result=words[i];
                    wordsSet.Add(words[i]);
                }
                else if(words[i].Length-words[i-1].Length>1){
                    break;
                }    
            }
        }
        return result;
    }
    public bool CompareString(string str1,string str2){
        for(int i=0;i<str1.Length;i++){
            if((int)str2[i]-(int)str1[i]<0){
                return true;
            }
            if((int)str2[i]-(int)str1[i]>0){
                return false;
            }
        }
        return false;
    }
}

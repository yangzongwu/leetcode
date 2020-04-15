public class Solution {
    public string[] UncommonFromSentences(string A, string B) {
        string[] strA=A.Split(" ");
        string[] strB=B.Split(" ");
        Dictionary<string,int> myDict=new Dictionary<string,int>();
        foreach(string str in strA){
            if(!myDict.ContainsKey(str)){
                myDict[str]=1;
            }
            else{
                myDict[str]+=1;
            }
        }
        foreach(string str in strB){
            if(!myDict.ContainsKey(str)){
                myDict[str]=1;
            }
            else{
                myDict[str]+=1;
            }
        }
        IList<string> result=new List<string>();
        foreach(KeyValuePair<string,int> kvp in myDict){
            if(kvp.Value==1){
                result.Add(kvp.Key);
            }
        }
        return result.ToArray();
    }
}

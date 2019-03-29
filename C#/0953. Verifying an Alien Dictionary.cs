public class Solution {
    public bool IsAlienSorted(string[] words, string order) {
        Dictionary<char,int> orderDict=new Dictionary<char,int>();
        for(int i=0;i<order.Length;i++){
            orderDict[order[i]]=i;
        }
        if(words.Length<=1){
            return true;
        }
        
        for(int i=1;i<words.Length;i++){
            if(!IsWordAlienSorted(words[i-1],words[i],orderDict)){
                return false;
            }
        }
        return true;
    }
    public bool IsWordAlienSorted(string wordA,string wordB,Dictionary<char,int> orderDict){
        for(int i=0;i<Math.Min(wordA.Length,wordB.Length);i++){
            if(orderDict[wordA[i]]>orderDict[wordB[i]]){
                return false;
            }
            else if(orderDict[wordA[i]]<orderDict[wordB[i]]){
                return true;
            }
        }
        if(wordA.Length<=wordB.Length){
            return true;
        }
        else{
            return false;
        }
    }
}

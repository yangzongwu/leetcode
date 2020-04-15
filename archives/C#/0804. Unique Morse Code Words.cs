public class Solution {
    public int UniqueMorseRepresentations(string[] words) {
        IList<string> morseList=new List<string>{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        Dictionary<char,string> morseDic=new Dictionary<char,string>();
        string s="abcdefghijklmnopqrstuvwxyz";
        for (int i=0;i<26;i++){
            morseDic[s[i]]=morseList[i];
        }
        
        HashSet<string> wordSet=new HashSet<string>();
        foreach(string word in words){
            string newWord=word.ToLower();
            string rep="";
            foreach(char c in newWord){
                rep+=morseDic[c];
            }
            wordSet.Add(rep);
        }
        return wordSet.Count;
    }
}

public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        Dictionary<char,int> magazineDict=new Dictionary<char,int>();
        foreach(char c in magazine){
            if(!magazineDict.ContainsKey(c)){
                magazineDict[c]=1;
            }
            else{
                magazineDict[c]+=1;
            }
        }
        bool flag=true;
        foreach(char c in ransomNote){
            if(!magazineDict.ContainsKey(c)){
                flag=false;
                break;
            }
            else{
                if(magazineDict[c]==0){
                    flag=false;
                    break;
                }
                else{
                    magazineDict[c]-=1;
                }
            }
        }
        return flag;
    }
}

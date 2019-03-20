public class Solution {
    public int LengthOfLastWord(string s) {
        string allchar="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
        int lenS=s.Length-1;
        while (lenS>=0 && s[lenS]==' '){
            lenS-=1;
        }
        int rep=0;
        for(int i=lenS;i>=0;--i){
            if(allchar.Contains(s[i])){
                rep+=1;
            }
            else{
                break;
            }
        }
        return rep;
    }
}

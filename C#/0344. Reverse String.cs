public class Solution {
    public int TitleToNumber(string s) {
        int rep=0;
        foreach(char c in s){
            int i=c-64;
            rep=rep*26+i;
        }
        return rep;
    }
}

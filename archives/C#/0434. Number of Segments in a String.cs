public class Solution {
    public int CountSegments(string s) {
        string[] t=s.Split(" ");
        int rep=0;
        foreach(string ss in t){
            if(ss.Length!=0){
                rep+=1;
            }
        }
        return rep;
    } 
}

public class Solution {
    public int NumJewelsInStones(string J, string S) {
        HashSet<char> JSet=new HashSet<char>(J.ToCharArray());
        int cnt=0;
        foreach(char s in S){
            if(JSet.Contains(s)){
                cnt+=1;
            }
        }
        return cnt;
    }
}

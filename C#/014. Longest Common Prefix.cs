public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if(strs.Length==0){
            return "";
        }
        int minStrLenth=strs[0].Length;
        
        for(int i=1;i<strs.Length;i++){
            minStrLenth=Math.Min(minStrLenth,strs[i].Length);
        }
        
        string rep="" ;
        for(int i=0;i<minStrLenth;i++){
            char target=strs[0][i];
            for(int j=1;j<strs.Length;j++){
                if(strs[j][i]!=target){
                    return rep;
                }
            }
            rep+=target;
        }
        return rep;
    }
}

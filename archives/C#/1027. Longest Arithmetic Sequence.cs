public class Solution {
    public int LongestArithSeqLength(int[] A) {
        Dictionary<int,Dictionary<int,int>> tmp=new Dictionary<int,Dictionary<int,int>>();
        
        int rep=2;
        for(int i=0;i<A.Length;i++){
            Dictionary<int,int> curDict=new Dictionary<int,int>();
            tmp[i]=curDict;
            for(int j=0;j<i;j++){
                if(!tmp[j].ContainsKey(A[i]-A[j])){
                    tmp[i][A[i]-A[j]]=2;
                }
                else{
                    tmp[i][A[i]-A[j]]=tmp[j][A[i]-A[j]]+1;
                    rep=Math.Max(tmp[i][A[i]-A[j]],rep);
                }
            }
        }
        return rep;
    }
}

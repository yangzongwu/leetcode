public class Solution {
    public IList<bool> PrefixesDivBy5(int[] A) {
        IList<bool> result=new List<bool>();
        int rep=0;
        for(int i=0;i<A.Length;i++){
            rep=rep*2+A[i];
            rep=rep%5;
            if(rep==0){
                result.Add(true);
            }
            else{
                result.Add(false);
            }
        }
        return result;
    }
    
}

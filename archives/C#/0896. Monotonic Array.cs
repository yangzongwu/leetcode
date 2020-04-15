public class Solution {
    public bool IsMonotonic(int[] A) {
        if(A.Length==1){return true;}
        int left=1;
        while (left<A.Length && A[left]==A[left-1]){
            left+=1;
        }
        if (left==A.Length){return true;}
        
        else if(A[left]>A[left-1]){
            for(int i=left;i<A.Length;i++){
                if (A[i]<A[i-1]){
                    return false;
                }
            }
            return true;
        }
        else{
            for(int i=left;i<A.Length;i++){
                if (A[i]>A[i-1]){
                    return false;
                }
            }
            return true;
        }
    }
}

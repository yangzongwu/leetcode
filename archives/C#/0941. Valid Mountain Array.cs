public class Solution {
    public bool ValidMountainArray(int[] A) {
        if(A.Length<3){return false;}
        int top=0;
        for(int i=1;i<A.Length;i++){
            if(A[i]==A[i-1]){
                return false;
            }
            else if(A[i]<A[i-1]){
                top=i-1;
                break;
            }
        }
        if(top==0){return false;}
        for(int i=top+1;i<A.Length;i++){
            if(A[i]>=A[i-1]){
                return false;
            }
        }
        return true;
    }
}

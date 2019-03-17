public class Solution {
    public int[] SortedSquares(int[] A) {
        for(int i=0;i<A.Length;i++){
            A[i]=A[i]*A[i];
        }
        Array.Sort(A);
        return A;
        
    }
}
//=======================================================================================
public class Solution {
    public int[] SortedSquares(int[] A) {
        int l=A.Length;
        int[] newA=new int[l];
        int left=0;
        int right=l-1;
        while (left<=right){
            if (A[left]*A[left]<A[right]*A[right]){
                newA[l-1]=A[right]*A[right];
                right-=1;
                l-=1;
            }
            else{
                newA[l-1]=A[left]*A[left];
                left+=1;
                l-=1;
            }
        }
        return newA;
        
    }
}

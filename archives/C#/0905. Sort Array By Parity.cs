public class Solution {
    public int[] SortArrayByParity(int[] A) {
        int left=0;
        int right=A.Length-1;
        while (left<A.Length && A[left]%2==0){
            left++;
        }
        while(right>left &&A[right]%2!=0){
            right--;
        }
        while(left<right){
            if ((A[left])%2==0){
                left++;
            }
            else{
                int tmp=A[left];
                A[left]=A[right];
                A[right]=tmp;
                right--;
            }
        }
        return A;
    }
}

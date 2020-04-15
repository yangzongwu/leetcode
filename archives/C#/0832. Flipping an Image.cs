public class Solution {
    public int[][] FlipAndInvertImage(int[][] A) {
        for(int i=0;i<A.Length;i++){
            A[i]=ReverseArray(A[i]);
        }
        for(int i=0;i<A.Length;i++){
            A[i]=Flip(A[i]);
        }
        return A;
    }
    public int[] ReverseArray(int[] nums){
        int left=0;
        int right=nums.Length-1;
        while(left<right){
            int tmp=nums[left];
            nums[left]=nums[right];
            nums[right]=tmp;
            left+=1;
            right-=1;
        }
        return nums;
    }
    public int[] Flip(int[] nums){
        for(int i=0;i<nums.Length;i++){
            nums[i]=nums[i]^1;
        }
        return nums;
    }
}

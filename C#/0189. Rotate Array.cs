public class Solution {
    public void Rotate(int[] nums, int k) {
        k=k%nums.Length;
        Reverse(nums,0,nums.Length-k-1);
        Reverse(nums,nums.Length-k,nums.Length-1);
        Reverse(nums,0,nums.Length-1);
        //return nums;
        
    }
    public int[] Reverse(int[] nums,int left,int right){
        while(left<right){
            int tmp=nums[left];
            nums[left]=nums[right];
            nums[right]=tmp;
            left+=1;
            right-=1;
        }
        return nums;
    }
}

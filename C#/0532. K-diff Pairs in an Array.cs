public class Solution {
    public int FindPairs(int[] nums, int k) {
        Array.Sort(nums);
        int left=0;
        int right=1;
        int rep=0;
        while(right<nums.Length){
            if(nums[right]-nums[left]>k){
                left++;
            }
            else if(nums[right]-nums[left]<k){
                right++;
            }
            else{
                rep++;
                int targetLeft=nums[left];
                while(left<nums.Length && nums[left]==targetLeft){
                    left++;
                }
            }
            if(left>=right){
                right=left+1;
            }
        }
        return rep;
    }
}

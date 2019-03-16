public class Solution {
    public int ArrayPairSum(int[] nums) {
        Array.Sort(nums);
        int result=0;
        for(int i=0;i<nums.Length;i+=2){
            result+=nums[i];
        }
        return result;
    }
}

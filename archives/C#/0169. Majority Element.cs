public class Solution {
    public int MajorityElement(int[] nums) {
        Array.Sort(nums);
        int i = nums.Length / 2;
        return nums[i];
    }
}

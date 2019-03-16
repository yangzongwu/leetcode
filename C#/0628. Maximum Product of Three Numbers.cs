public class Solution {
    public int MaximumProduct(int[] nums) {
        Array.Sort(nums);
        int rep;
        int len_nums=nums.Length;
        rep=Math.Max(nums[len_nums-1]*nums[len_nums-2]*nums[len_nums-3],nums[len_nums-1]*nums[0]*nums[1]);
        return rep;
            
    }
}

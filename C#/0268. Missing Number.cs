public class Solution {
    public int MissingNumber(int[] nums) {
        int len_nums = nums.Length;
        int sum_nums = 0;
        foreach(int num in nums)
        {
            sum_nums += num;
        }
        return (1 + len_nums) * len_nums / 2 - sum_nums;
    }
}

public class Solution {
    public int ThirdMax(int[] nums) {
        if (nums.Length == 1)
            {
                return nums[0];
            }
            else if (nums.Length ==2)
            {
                return Math.Max(nums[0], nums[1]);
            }

            Int64 first = Int64.MinValue;
            Int64 second = Int64.MinValue;
            Int64 third = Int64.MinValue;  

            for(int i=0;i< nums.Length; i++){
                if (nums[i]== third || nums[i]== second || nums[i] == first)
                {
                    continue;
                }
                if (nums[i] > third)
                {
                    first = second;
                    second = third;
                    third = nums[i];
                }
                else if (nums[i] > second)
                {
                    first = second;
                    second = nums[i];
                }
                else if (nums[i] > first)
                {
                    first = nums[i];
                }
            }
            if (first == Int64.MinValue)
            {
                return (int)third;
            }
            else
            {
                return (int)first;
            }
        }
}

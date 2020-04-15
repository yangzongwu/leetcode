public class Solution {
    public void MoveZeroes(int[] nums) {
        int left = 0;         
        while (left < nums.Length && nums[left] != 0)
        {
            left++;
        }
        if (left < nums.Length)
        {
            int right = left;
            while (right < nums.Length)
            {
                while (right < nums.Length && nums[right] == 0)
                {
                    right++;
                }
                if (right == nums.Length)
                {
                    break;
                }
                else
                {
                    int tmp = nums[right];
                    nums[right] = nums[left];
                    nums[left] = tmp;
                    right++;
                }
                while (left < nums.Length && nums[left] != 0)
                {
                    left++;
                }
                if (left > right)
                {
                    right = left;
                } 
            }

        }
    }
}

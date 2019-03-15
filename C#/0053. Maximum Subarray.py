public class Solution {
    public int MaxSubArray(int[] nums) {
        int rep = nums[0];
        int tmp = 0;
        foreach(int i in nums)
        {
            tmp += i;
            rep = Math.Max(tmp, rep);
            if (tmp < 0)
            {
                tmp = 0;
            }
        }
        return rep;    
    }
}

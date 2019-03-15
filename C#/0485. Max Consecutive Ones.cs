public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int rep = 0;
        int cnt = 0;
        foreach (int num in nums)
        {
            if (num == 1)
            {
                cnt += 1;
            }
            else if(cnt>0)
            {
                rep = Math.Max(rep, cnt);
                cnt = 0;
            }
        }
        return Math.Max(rep, cnt);
    }
}

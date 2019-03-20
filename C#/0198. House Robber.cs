public class Solution {
    public int Rob(int[] nums) {
        int lenNums=nums.Length;
        if(lenNums==0){
            return 0;
        }
        if(lenNums==1){
            return nums[0];
        }
        IList<int> dp=new List<int>();
        dp.Add(0);
        dp.Add(nums[0]);
        for(int i=2;i<lenNums+1;i++){
            dp.Add(Math.Max(dp[i-1],dp[i-2]+nums[i-1]));
        }
        return Math.Max(dp[lenNums],dp[lenNums-1]);
    }
}

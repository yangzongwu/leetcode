public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int[] dp=new int[cost.Length+1];
        dp[0]=0;
        dp[1]=cost[0];
        for(int i=1;i<cost.Length;i++){
            dp[i+1]=cost[i]+Math.Min(dp[i],dp[i-1]);
        }
        return Math.Min(dp[dp.Length-1],dp[dp.Length-2]);
    }
}

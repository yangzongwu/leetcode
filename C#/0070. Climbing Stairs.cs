public class Solution {
    public int ClimbStairs(int n) {
        //dp[n]=dp[n-1]+dp[n-2]
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        if(n==2){
            return 2;
        }
        IList<int> dp=new List<int>();
        dp.Add(0);
        dp.Add(1);
        dp.Add(2);
        for(int i=3;i<n+1;i++){
            dp.Add(dp[i-1]+dp[i-2]);
        }
        return dp[dp.Count-1];
        
    }
}

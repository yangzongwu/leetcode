public class Solution {
    public int NumTrees(int n) {
        /*
        1   1
        2   f(1)+f(1)=2
        3   f(0)f(2)+f(1)f(1)+f(2)f(0)=5
        4   f(0)(3)+f(1)f(2)+f(2)f(1)+f(3)f(0)=...
        5   
        f(n)=f(0)f(n-1)+f(1)f(n-1-1)+...+f(i)f(n-1-i)+...+f(n-1)f(0)
        */
        
        List<int> dp=new List<int>();
        dp.Add(1);
        dp.Add(1);
        for(int i=2;i<n+1;i++){
            int tmp=0;
            for(int j=0;j<i;j++){
                tmp+=dp[j]*dp[i-1-j];
            }
            dp.Add(tmp);
        }
        return dp[n];
    }
}

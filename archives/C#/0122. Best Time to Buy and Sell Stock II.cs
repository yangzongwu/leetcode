public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length == 0)
            {
                return 0;
            }
            int rep = 0;
            for(int i = 1; i < prices.Length; i++)
            {
                if (prices[i] > prices[i - 1])
                {
                    rep += prices[i] - prices[i - 1];
                }
            }
            return rep;        
    }
}

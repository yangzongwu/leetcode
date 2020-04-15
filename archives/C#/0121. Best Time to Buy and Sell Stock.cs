public class Solution {
    public int MaxProfit(int[] prices) {
        int rep = 0;
        if (prices.Length == 0)
        {
            return 0;
        }
        else
        {
            int minprice = prices[0];
            for (int i = 1; i < prices.Length; i++)
            {
                if (prices[i] < minprice)
                   { 
                    minprice = prices[i];
                }
                else
                {
                    rep = Math.Max(rep, prices[i] - minprice);
                }                                  
            }
                return rep;
            }
        }    
    }

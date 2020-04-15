public class Solution {
    public int MaxProduct(int[] nums) {
        if(nums.Length==0)
            return 0;
        int curMax=1;
        int curMin=1;
        int maxProduct=nums[0];
        foreach(int num in nums){
            int preMax=curMax;
            curMax=Math.Max(num,Math.Max(num*preMax,num*curMin));
            curMin=Math.Min(num,Math.Min(num*preMax,num*curMin));
            maxProduct=Math.Max(maxProduct,curMax);
            //Console.WriteLine("{0},{1},{2}",curMax,curMin,maxProduct);
        }
        return maxProduct;
    }
}

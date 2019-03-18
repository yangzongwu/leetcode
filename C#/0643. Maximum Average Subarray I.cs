public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        double rep=0;
        for(int i=0;i<k;i++){
            rep+=nums[i];
        }
        int left=0;
        int right=k;
        double result=rep;
        
        while (right<nums.Length){
            rep=rep-nums[left]+nums[right];
            result=Math.Max(result,rep);
            left+=1;
            right+=1;
        }
        
        return result/k;;
    }
}

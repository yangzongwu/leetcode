public class Solution {
    public int FindLengthOfLCIS(int[] nums) {
        if (nums.Length==0){
            return 0;
        }
        int rep=0;
        int tmp=1;
        for(int i=1;i<nums.Length;i++){
            if (nums[i]>nums[i-1]){
                tmp+=1;
            }
            else{
                rep=Math.Max(rep,tmp);
                tmp=1;
            }
        }
        return Math.Max(rep,tmp);
    }
}

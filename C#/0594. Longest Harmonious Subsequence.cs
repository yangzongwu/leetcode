public class Solution {
    public int FindLHS(int[] nums) {
        if(nums.Length<=1){
            return 0;
        }
        Array.Sort(nums);
        int left=0;
        int target=nums[left];
        int rep=0;
        for(int i=1;i<nums.Length;i++){
            if(nums[i]-target>1){
                if (nums[i-1]-target==1){
                    rep=Math.Max(rep,i-left);
                }
                while(nums[left]==target){
                    left++;
                }
                target=nums[left];
            }
        }
        if (nums[nums.Length-1]-target==1){
            rep=Math.Max(rep,nums.Length-left);
        }
        
        return rep;
        
    }
}

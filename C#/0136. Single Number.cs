public class Solution {
    public int SingleNumber(int[] nums) {
        int rep=nums[0];
        for(int i=1;i<nums.Length;i++){
            rep^=nums[i];
        }
        return rep;
    }
}

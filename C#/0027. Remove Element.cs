public class Solution {
    public int RemoveElement(int[] nums, int val) {        
        int cur=0;
        for (int i=0;i<nums.Length;i++){
            if (nums[i]!=val){
                nums[cur]=nums[i];
                cur++;
            }
        }
        return cur;
    }
}

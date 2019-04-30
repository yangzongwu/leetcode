public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if(nums.Length!=0){
            int left=0;
            int target=nums[0];
            int cnt=0;
            for(int i=0;i<nums.Length;i++){
                if(nums[i]==target && cnt!=2){
                    nums[left]=target;
                    cnt++;
                    left++;
                }
                else if(nums[i]==target && cnt==2){
                    continue;
                }
                else{
                    target=nums[i];
                    nums[left]=target;
                    left++;
                    cnt=1;
                }
            }
            return left;
        }
        return 0;
    }
}

public class Solution {
    public void SortColors(int[] nums) {
        int left=0;
        while(left<nums.Length && nums[left]==0)
            left++;
        int right=nums.Length-1;
        while(right>left && nums[right]==2)
            right--;
        int mid=left;
        while(mid<=right){
            if(nums[mid]==1)
                mid++;
            else if(nums[mid]==0){
                int tmp=nums[mid];
                nums[mid]=nums[left];
                nums[left]=tmp;
                left++;
                mid++;
            }
            else{
                int tmp=nums[mid];
                nums[mid]=nums[right];
                nums[right]=tmp;
                right--;
            }
        }
    }
}

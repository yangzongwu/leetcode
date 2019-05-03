public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int sum=nums[0]+nums[1]+nums[2];
        int i=0;
        while(i<nums.Length-2){
            int tmpSum=ThreeSumClosest(nums,i,target);
            sum=Math.Abs(sum-target)>Math.Abs(tmpSum-target)?tmpSum:sum;
            i++;
            while(i<nums.Length-2 && nums[i]==target){
                i++;
            }
        }
        return sum;
    }
    public int ThreeSumClosest(int[] nums,int i, int target){
        int left=i+1;
        int right=nums.Length-1;
        int sum=nums[0]+nums[1]+nums[2];
        while(left<right){
            int curSum=nums[i]+nums[left]+nums[right];
            sum=Math.Abs(sum-target)>Math.Abs(curSum-target)?curSum:sum;
            if(curSum>target)
                right--;
            else
                left++;
        }
        return sum;
    }
}

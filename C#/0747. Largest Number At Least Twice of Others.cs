public class Solution {
    public int DominantIndex(int[] nums) {
        int first=int.MinValue;
        int second=int.MinValue;
        int loc=0;
        for (int i=0;i<nums.Length;i++){
            if (nums[i]>first){
                second=first;
                first=nums[i];
                loc=i;
            }
            else if (nums[i]<first && nums[i]>second){
                second=nums[i];
            }
        }
        if(second==int.MinValue){
            return 0;
        }
        if(first>=second*2){
            return loc;
        }
        else{
            return -1;
        }
    }
}

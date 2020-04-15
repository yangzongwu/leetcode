public class Solution {
    public int PivotIndex(int[] nums) {
        int[] numleft=new int[nums.Length];
        int[] numright=new int[nums.Length];
        int leftsum=0;
        for(int i=0;i<nums.Length;i++){
            numleft[i]=leftsum;
            leftsum+=nums[i];
        }
        int rightsum=0;
        for(int i=nums.Length-1;i>=0;i--){
            numright[i]=rightsum;
            rightsum+=nums[i];
        }
        for (int i=0;i<nums.Length;i++){
            if(numleft[i]==numright[i]){
                return i;
            }
        }
        return -1;
    }
}

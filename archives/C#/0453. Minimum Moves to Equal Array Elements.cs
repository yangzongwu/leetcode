public class Solution {
    public int MinMoves(int[] nums) {
        int rep=0;
        int minNums=nums.Min();
        foreach(int num in nums){
            rep+=num-minNums;
        }
        return rep;
    }
}

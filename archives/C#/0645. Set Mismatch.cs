public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int[] rep=new int[2];
        int total=(1+nums.Count())*nums.Count()/2;
        int numsSum=nums.Sum();
        HashSet<int> numsSet=new HashSet<int>(nums);
        int numssetSum=numsSet.Sum();
        int SN=total-numssetSum;
        int FN=numsSum-numssetSum;
        rep[0]=(FN);
        rep[1]=(SN);
        
        return rep;
    }
}

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> numsDic=new Dictionary<int,int>();
        for(int i=0;i<nums.Length;i++){
            if (numsDic.ContainsKey(target-nums[i])){
                return new int[]{numsDic[target-nums[i]],i};
            }
            numsDic[nums[i]]=i;
        }
        return new int[0];
    }
}

public class Solution {
    public int[] NextGreaterElement(int[] findNums, int[] nums) {
        Dictionary<int,int> nextGreaterNumDict= new Dictionary<int,int>();
        for(int i=0;i<nums.Length;i++){
            int flag=-1;
            for(int j=i+1;j<nums.Length;j++){
                if(nums[j]>nums[i]){
                    flag=nums[j];
                    break;
                }
            }
            nextGreaterNumDict[nums[i]]=flag;
        }
        int[] result=new int[findNums.Length];
        for(int i=0;i<findNums.Length;i++){
            result[i]=nextGreaterNumDict[findNums[i]];
        }
        return result;
    }
}

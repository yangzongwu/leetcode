public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        Dictionary<int,int> numsDict=new Dictionary<int,int>();
        bool flag=false;
        for(int i=0;i<nums.Length;i++){
            if(!numsDict.ContainsKey(nums[i])){
                numsDict.Add(nums[i],i);
            }
            else{
                if(i-numsDict[nums[i]]<=k){
                    flag=true;
                    break;
                }
                else{
                    numsDict[nums[i]]=i;
                }
            }
        }
        return flag;
    }
}

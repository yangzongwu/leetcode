public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> threeSumList=new List<IList<int>>();
        Array.Sort(nums);
        int cur=0;
        while(cur<nums.Length-1){
            IList<IList<int>> rep=new List<IList<int>>();
            rep=TwoSum(nums,cur);
            foreach(var list in rep){
                threeSumList.Add(list);
            }
            int target=nums[cur];
            cur++;
            while(cur<nums.Length && nums[cur]==target){
                cur++;
            }
        }
        return threeSumList;
    }
    public IList<IList<int>> TwoSum(int[] nums,int cur){
        IList<IList<int>> rep=new List<IList<int>>();
        int left=cur+1;
        int right=nums.Length-1;
        while(left<right){
            if(nums[left]+nums[right]+nums[cur]>0){
                int curr=nums[right];
                while(right>left && nums[right]==curr){
                    right--;
                }
            }
            else if (nums[left]+nums[right]+nums[cur]<0){
                int curl=nums[left];
                while(left<right && nums[left]==curl){
                    left++;
                }
            }
            else{        
                rep.Add(new List<int>{nums[cur],nums[left],nums[right]});
                int curl=nums[left];
                while(left<right && nums[left]==curl){
                    left++;
                }
            }
        }
        return rep;
    } 
}

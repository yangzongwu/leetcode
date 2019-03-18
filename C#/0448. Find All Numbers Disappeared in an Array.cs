public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        int i=0;
        while(i<nums.Length){
            if (nums[i]-1!=i && nums[nums[i]-1]!=nums[i]){
                int tmp=nums[i];
                nums[i]=nums[tmp-1];
                nums[tmp-1]=tmp;
            }
            else{
                i+=1;
            }
        }
        IList<int> rep=new List<int>();
        for(int j=0;j<nums.Length;j++){
            if (nums[j]-1!=j){
                rep.Add(j+1);
            }
        }
        return rep;
    }
}

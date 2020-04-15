public class NumArray {
    
    IList<int> rep=new List<int>();
    public NumArray(int[] nums) {
        int sumNums=0;
        for(int i=0;i<nums.Length;i++){
            rep.Add(sumNums);
            sumNums+=nums[i];
        }
        rep.Add(sumNums);
    }
    
    public int SumRange(int i, int j) {
        return rep[j+1]-rep[i];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(i,j);
 */

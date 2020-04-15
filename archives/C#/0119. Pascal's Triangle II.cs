public class Solution {
    public IList<int> GetRow(int rowIndex) {   
        IList<int> nums=new List<int>();
        nums.Add(1);
        if (rowIndex==0){
            return nums;
        }
        nums.Add(1);
        
        IList<int> prenums=nums;
        for(int i=2;i<rowIndex+1;i++){
            IList<int> curnums=new List<int>{1};
            for(int j=0;j<prenums.Count-1;j++){
                curnums.Add(prenums[j]+prenums[j+1]);
            }
            curnums.Add(1);
            prenums=curnums;
        }
        
        return prenums;
    }
}

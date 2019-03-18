public class Solution {
    public IList<IList<int>> Generate(int numRows) {       
        IList<IList<int>> nums=new List<IList<int>>();
        if (numRows==0){
            return nums;
        }
        nums.Add(new List<int>(){1});
        if(numRows==1){
            return nums;
        }
        IList<int> prenums= new List<int>(){1,1};
        nums.Add(prenums);
            
        for(int i=3;i<numRows+1;i++){
            IList<int> curnums=new List<int>{1};
            for(int j=0;j<prenums.Count-1;j++){
                curnums.Add(prenums[j]+prenums[j+1]);
            }
            curnums.Add(1);
            nums.Add(curnums);
            prenums=curnums;
        }
        
        return nums;
        
        
    }
}

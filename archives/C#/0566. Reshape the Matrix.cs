public class Solution {
    public int[,] MatrixReshape(int[,] nums, int r, int c) {
        int row=nums.GetLength(0);    
        int column=nums.GetLength(1);
        if(row*column!=r*c){
            return nums;
        }
        
        int[,] newnums=new int[r,c];
        int newrow=0;
        int newcolumn=0;
        for (int row1=0;row1<row;row1++){
            for(int column1=0;column1<column;column1++){
                if (newcolumn==c){
                    newcolumn=0;
                    newrow+=1;
                }
                newnums[newrow,newcolumn]=nums[row1,column1];
                newcolumn+=1;
            }
        }
        return newnums;
    }
}

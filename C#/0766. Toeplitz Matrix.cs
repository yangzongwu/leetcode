public class Solution {
    public bool IsToeplitzMatrix(int[,] matrix) {
        for (int row=0;row<matrix.GetLength(0);row++){
            if (IsSameValue(row,0,matrix)==false){
                return false;
            }
        }
        for (int column=0;column<matrix.GetLength(1);column++){
            if (IsSameValue(0,column,matrix)==false){
                return false;
            }
        }
        return true;
    }
    public bool IsSameValue(int row,int column,int[,] matrix){
        int target=matrix[row,column];
        row+=1;
        column+=1;
        while(row<matrix.GetLength(0) && column<matrix.GetLength(1)){
            if (matrix[row,column]!=target){
                return false;
            }
            row++;
            column++;
        }
        return true;
    }
}

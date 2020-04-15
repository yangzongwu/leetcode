public class Solution {
    public void SetZeroes(int[][] matrix) {
        int rowFlag=1;
        int colFlag=1;
        foreach(var num in matrix[0]){
            if(num==0){
                rowFlag=0;
                break;
            }
        }
        
        foreach(var submatrix in matrix){
            if(submatrix[0]==0){
                colFlag=0;
                break;
            }
        }
        
        for(int row=1;row<matrix.Length;row++){
            for(int col=1;col<matrix[0].Length;col++){
                if(matrix[row][col]==0){
                    matrix[0][col]=0;
                    matrix[row][0]=0;
                }
            }
        }
        
        for(int row=1;row<matrix.Length;row++){
            if(matrix[row][0]==0){
                for(int col=0;col<matrix[0].Length;col++)
                    matrix[row][col]=0;
            }
        }
        
        for(int col=1;col<matrix[0].Length;col++){
            if(matrix[0][col]==0){
                for(int row=0;row<matrix.Length;row++)
                    matrix[row][col]=0;
            }
        }
        
        if(matrix[0][0]==0 || rowFlag==0){
            for(int col=1;col<matrix[0].Length;col++)
                matrix[0][col]=0;
        }
        if(matrix[0][0]==0 || colFlag==0){
            for(int row=1;row<matrix.Length;row++)
                matrix[row][0]=0;
        }
        if(rowFlag==0 || colFlag==0)
            matrix[0][0]=0;
        
    }
}
    
    

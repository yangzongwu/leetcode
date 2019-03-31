public class Solution {
    public int NumEnclaves(int[][] A) {
        for(int row=0;row<A.Length;row++){
            if(A[row][0]==1){
                A=FillA(A,row,0);
            }
            if(A[row][A[0].Length-1]==1){
                A=FillA(A,row,A[0].Length-1);
            }
        }
        for(int column=0;column<A[0].Length;column++){
            if(A[0][column]==1){
                A=FillA(A,0,column);
            }
            if(A[A.Length-1][column]==1){
                A=FillA(A,A.Length-1,column);
            }
        }
        
        int rep=0;
        for(int row=0;row<A.Length;row++){
            for(int column=0;column<A[0].Length;column++){
                if(A[row][column]==1){
                    rep++;
                }
            }
        }
        return rep;
    }
    
    public int[][] FillA(int[][] A,int row,int column){
        A[row][column]='X';
        if(row-1>=0 && A[row-1][column]==1){
            FillA(A,row-1,column);
        }
        if(column-1>=0 && A[row][column-1]==1){
            FillA(A,row,column-1);
        }
        if(row+1<A.Length &&A[row+1][column]==1){
            FillA(A,row+1,column);
        }
        if(column+1<A[0].Length && A[row][column+1]==1){
            FillA(A,row,column+1);
        }
        return A;
    }
}

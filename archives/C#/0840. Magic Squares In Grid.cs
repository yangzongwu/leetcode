public class Solution {
    public int NumMagicSquaresInside(int[][] grid) {
        int result=0;
        for (int row=0;row<grid.Length-2;row++){
            for (int column=0;column<grid[0].Length-2;column++){
                if (isMagicSquare(grid,row,column)){
                    result+=1;
                }
            }
        }
        return result;
    }
    
    public bool isMagicSquare(int[][] grid,int row,int column){
        HashSet<int> hashset = new HashSet<int>(new int[]{1,2,3,4,5,6,7,8,9});
        for(int i=row;i<row+3;i++){
            for(int j=column;j<column+3;j++){
                hashset.Remove(grid[i][j]);
            }
        }
        
        if (hashset.Count!=0){
            return false;
        }
            
        int target=grid[row][column]+grid[row+1][column]+grid[row+2][column];
        if(grid[row][column+1]+grid[row+1][column+1]+grid[row+2][column+1]!=target){
            return false;
        }
        else if(grid[row][column+2]+grid[row+1][column+2]+grid[row+2][column+2]!=target){
            return false;
        }
        else if(grid[row][column]+grid[row][column+1]+grid[row][column+2]!=target){
            return false;
        }
        else if(grid[row+1][column]+grid[row+1][column+1]+grid[row+1][column+2]!=target){
            return false;
        }
        else if(grid[row+2][column]+grid[row+2][column+1]+grid[row+2][column+2]!=target){
            return false;
        }
        
        else if(grid[row][column]+grid[row+1][column+1]+grid[row+2][column+2]!=target){
            return false;
        }
        else if(grid[row][column+2]+grid[row+1][column+1]+grid[row+2][column]!=target){
            return false;
        }
        return true;
    }
}

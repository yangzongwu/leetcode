public class Solution {
    public int IslandPerimeter(int[,] grid) {
        for(int row=0;row<grid.GetLength(0);row++){
            for(int column=0;column<grid.GetLength(1);column++){
                if(grid[row,column]==1){
                    return CalIslandPerimeter(grid,row,column);
                }
            }
        }
        return 0;
    }
    public int CalIslandPerimeter(int[,] grid,int row,int column){
        int rep=4;
        grid[row,column]='X';
        if (row-1>=0){
            if(grid[row-1,column]==1){
                rep+=CalIslandPerimeter(grid,row-1,column)-1;
            }
            else if (grid[row-1,column]=='X'){
                rep--;
            }
        }
        if (column-1>=0){
            if(grid[row,column-1]==1){
                rep+=CalIslandPerimeter(grid,row,column-1)-1;
            }
            else if (grid[row,column-1]=='X'){
                rep--;
            }
        }
        if (row+1<grid.GetLength(0)){
            if(grid[row+1,column]==1){
                rep+=CalIslandPerimeter(grid,row+1,column)-1;
            }
            else if (grid[row+1,column]=='X'){
                rep--;
            }
        } 
        if (column+1<grid.GetLength(1)){
            if(grid[row,column+1]==1){
                rep+=CalIslandPerimeter(grid,row,column+1)-1;
            }
            else if (grid[row,column+1]=='X'){
                rep--;
            }
        }
        return rep;
    }
}

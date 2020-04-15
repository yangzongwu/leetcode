public class Solution {
    public int SurfaceArea(int[][] grid) {
        int rep=0;
        for(int row=0;row<grid.Length;row++){
            for(int column=0;column<grid[row].Length;column++){
                if(grid[row][column]!=0){
                    rep+=CalSurfaceArea(row,column,grid);
                }
            }
        }
        return rep;
    }
    
    public int CalSurfaceArea(int row,int column,int[][] grid){
        int rep=2+4*grid[row][column];
        if (row-1>=0 && grid[row-1][column]!=0){
            rep-=Math.Min(grid[row][column],grid[row-1][column]);
        }
        if (column-1>=0 && grid[row][column-1]!=0){
            rep-=Math.Min(grid[row][column],grid[row][column-1]);
        }
        if (row+1<grid.Length && grid[row+1][column]!=0){
            rep-=Math.Min(grid[row][column],grid[row+1][column]);
        }
        if (column+1<grid[row].Length && grid[row][column+1]!=0){
            rep-=Math.Min(grid[row][column],grid[row][column+1]);
        }
        return rep;
        
    }
}

public class Solution {
    public int NumIslands(char[][] grid) {
        int rep=0;
        for(int row=0;row<grid.Length;row++){
            for(int col=0;col<grid[0].Length;col++){
                if(grid[row][col]=='1'){
                    rep++;
                    ReFillIslands(grid,row,col);
                }
            }
        }
        return rep;
    }
    public void ReFillIslands(char[][] grid,int row,int col){
        grid[row][col]='X';
        if(row-1>=0 && grid[row-1][col]=='1')
            ReFillIslands(grid,row-1,col);
        if(col-1>=0 && grid[row][col-1]=='1')
            ReFillIslands(grid,row,col-1);
        if(row+1<grid.Length && grid[row+1][col]=='1')
            ReFillIslands(grid,row+1,col);
        if(col+1<grid[0].Length && grid[row][col+1]=='1')
            ReFillIslands(grid,row,col+1);
    }
}

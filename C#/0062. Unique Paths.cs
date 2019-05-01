public class Solution {
    public int UniquePaths(int m, int n) {
        var grid=new int[m,n];
        grid[0,0]=1;
        for(int row=1;row<m;row++){
            grid[row,0]=1;
        }
        for(int col=1;col<n;col++){
            grid[0,col]=1;
        }
            
        
        for(int row=1;row<m;row++){
            for(int col=1;col<n;col++){
                grid[row,col]=grid[row-1,col]+grid[row,col-1];
            }
        }
        return grid[m-1,n-1];
    }
}

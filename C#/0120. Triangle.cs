public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {
        for(int i=1;i<triangle.Count();i++){
            int len=triangle[i].Count();
            triangle[i][0]+=triangle[i-1][0];
            triangle[i][len-1]+=triangle[i-1][len-2];
            for(int j=1;j<len-1;j++){
                triangle[i][j]+=Math.Min(triangle[i-1][j-1],triangle[i-1][j]);
            }
        }
        return triangle[triangle.Count-1].Min();
    }
}

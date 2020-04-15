public class Solution {
    public int[] ConstructRectangle(int area) {
        int W=1;
        int L=area;
        for(int i=W+1;i*i<=area;i++){
            if (area%i==0 && Math.Abs(area/i-i)<Math.Abs(W-L)){
                W=i;
                L=area/i;
            }
        }
        return new int[]{L,W};
    }
}

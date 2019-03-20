public class Solution {
    public int TrailingZeroes(int n) {
        int tmp=0;
        while(n>=5){
            n=n/5;
            tmp+=n;
        }
        return tmp;
    }
}

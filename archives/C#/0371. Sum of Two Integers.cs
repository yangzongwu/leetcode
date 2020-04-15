public class Solution {
    public int GetSum(int a, int b) {
        for(int i=0;i<32;i++){
            int tmp=a&b;
            a=a^b;
            b=tmp<<1;
        }
        return a;
    }
}

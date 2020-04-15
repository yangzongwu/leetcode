public class Solution {
    public bool IsPowerOfTwo(int n) {
        if (n<=0){
            return false;
        }
        int rep=0;
        while(n!=0){
            rep+=n&1;
            n=n>>1;
        }
        return rep==1;
    }
}

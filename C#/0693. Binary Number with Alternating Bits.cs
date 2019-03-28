public class Solution {
    public bool HasAlternatingBits(int n) {
        int prev=(n&1);
        n=n>>1;
        while(n!=0){
            if(((n&1)^prev)!=1){
                return false;
            }
            prev=n&1;
            n=n>>1;
        }
        return true;
    }
}

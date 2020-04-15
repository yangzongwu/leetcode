public class Solution {
    public uint reverseBits(uint n) {
        uint rep=0;
        for(int i=0;i<32;i++){
            uint tmp=(n&1);
            rep=(rep<<1)+tmp;
            n=n>>1;
        }
        return rep;
    }
}

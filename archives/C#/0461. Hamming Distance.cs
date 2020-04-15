public class Solution {
    public int HammingDistance(int x, int y) {
        int z=x^y;
        int rep=0;
        while(z!=0){
            if((z&1)==1){
                rep+=1;
            }
            z=z>>1;
        }
        return rep;
    }
}

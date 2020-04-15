public class Solution {
    public bool IsPowerOfThree(int n) {
        if (n<=0){
            return false;
        }
        int rep=3;
        while(rep<(int.MaxValue/3)){
            rep*=3;
        }
        return rep%n==0;
    }
}

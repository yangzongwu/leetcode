public class Solution {
    public bool IsPalindrome(int x) {
        if(x<0){
            return false;
        }
        int target=x;
        int rep=0;
        while(x>0){
            int tmp=x%10;
            rep=rep*10+tmp;
            x=x/10;
        }
        return rep==target;
    }
}

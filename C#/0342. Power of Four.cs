public class Solution {
    public bool IsPowerOfFour(int num) {
        string s="1010101010101010101010101010101";
        int x=Convert.ToInt32(s,2);
        return ((num&x)!=0 && (num&(num-1))==0)?true:false;
    }
}

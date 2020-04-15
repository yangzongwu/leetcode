public class Solution {
    public int ArrangeCoins(int n) {
        if(n==0||n==1){
            return n;
        }
        long left=0;
        long right=n;
        while (left<=right){
            long mid=left+(right-left)/2;
            long tmp=(1+mid)*mid/2;
            if (tmp==n){
                return (int)mid;
            }
            else if(tmp>n){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return (int)right;
        
    }
}

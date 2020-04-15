public class Solution {
    public int MySqrt(int x) {
        if(x==1){
            return 1;
        }
        long left=0;
        long right=x/2;
        long mid;
        long result=0;
        while(left<=right){
            mid=(left+right)/2;

            if(mid*mid==x){
                result=mid;
                break;
            }
            if(mid*mid>int.MaxValue){
                right=mid-1;
            }
            else if(mid*mid>x){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        
        if(result==0){
            result=right;
        }
        return (int)result;
    }
}

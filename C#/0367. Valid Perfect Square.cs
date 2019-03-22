public class Solution {
    public bool IsPerfectSquare(int num) {
        if(num<0){
            return false;
        }
        bool flag=false;
        int left=1;
        int right=num;
        double tmp=Math.Sqrt(int.MaxValue);
        while(left<=right){
            int mid=left+(right-left)/2;
            if (mid>tmp){
                right=mid-1;
            }
            else{
                if(mid*mid==num){
                    return true;
                }
                else if(mid*mid>num){
                    right=mid-1;
                }
                else{
                    left=mid+1;
                }
            }
            
        }
        return flag;
    }
}

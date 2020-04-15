public class Solution {
    public double MyPow(double x, int n) {
        double m=n;
        if(n<0){
            m=-m;
            x=1/x;
        }
        double result=1;
        while(m>0){
            double tmp=x;
            int cnt=1;
            while(cnt<m-cnt){
                tmp*=tmp;
                cnt+=cnt;
            }
            m=m-cnt;
            result*=tmp;
        }
        return result;
    }
}

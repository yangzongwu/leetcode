public class Solution {
    public int Reverse(int x) {
        int flag=1;
        if(x<0){
            flag=-1;
            x=-x;
        }
        
        long y=0;
        while (x>0){
            int tmp=x%10;
            y=y*10+tmp;
            x=x/10;
        }
        
        if(flag==-1){
            y=-y;
        }
        
        if(y>int.MaxValue||y<int.MinValue ){
            return 0;
        }
        return (int)y;
    }
}

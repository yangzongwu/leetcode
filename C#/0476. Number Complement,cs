public class Solution {
    public int FindComplement(int num) {
        int flag=int.MaxValue/2+1;
        int rep=0;
        int cnt=0;
        while(num!=0){
            int tmp=num&1;
            tmp=(tmp^1)<<cnt;
            rep|=tmp;
            cnt+=1;
            num>>=1;
        }
        return rep;
        
    }
}

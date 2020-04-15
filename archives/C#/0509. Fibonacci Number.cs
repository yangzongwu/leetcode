public class Solution {
    public int Fib(int N) {
        if(N==0){return 0;}
        if(N==1){return 1;}
        int[] rep=new int[N+1];
        rep[0]=0;
        rep[1]=1;
        for(int i=2;i<=N;i++){
            rep[i]=rep[i-1]+rep[i-2];
        }
        return rep[N];
    }
}

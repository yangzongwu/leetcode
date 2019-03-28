public class Solution {
    public int CountPrimeSetBits(int L, int R) {
        int[] nums=new int[]{2,3,5,7,11,13,17,19,23,29};
        HashSet<int> primes=new HashSet<int>(nums);
        int cnt=0;
        for(int i=L;i<=R;i++){
            if(IsPrimes(i,primes)){
                cnt++;
            }
        }
        return cnt;
    }
    public bool IsPrimes(int i,HashSet<int> primes){
        int rep=0;
        while(i!=0){
            rep+=i&1;
            i=i>>1;
        }
        return primes.Contains(rep);
    }
}

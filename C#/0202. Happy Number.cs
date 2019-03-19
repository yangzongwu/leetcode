public class Solution {
    public bool IsHappy(int n) {
        HashSet<int> setN=new HashSet<int>(){0,1};
        while(!setN.Contains(n)){
            setN.Add(n);
            n=CalHappyNumber(n);
        }
        if(n==1){
            return true;
        }
        return false;
    }
    
    public int CalHappyNumber(int n){
        int rep=0;
        if(n<10){
            return n*n;
        }
        while(n>0){
            int tmp=n%10;
            rep+=tmp*tmp;
            n=n/10;
        }
        return rep;
    }
}

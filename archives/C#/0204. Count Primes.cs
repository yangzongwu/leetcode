public class Solution {
    public int CountPrimes(int n) {
        if(n==0 || n==1){
            return 0;
        }
        int[] nums=new int[n];
        nums[0]=1;
        nums[1]=1;
        for(int i=2;i<=(n-1)/2;i++){
            if(nums[i]==0){
                int j=2;
                while(i*j<n){
                    nums[i*j]=1;
                    j+=1;
                }
            }
        }
        int rep=0;
        foreach(int num in nums){
            if (num==0){
                rep+=1;
            }
        }
        return rep;
    }
}

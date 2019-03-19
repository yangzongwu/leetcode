public class Solution {
    public int RepeatedNTimes(int[] A) {
        int cnt=1;
        int flag=A[0];
        for(int i=1;i<A.Length;i++){
            if(A[i]==flag){
                cnt+=1;
            }
            else{
                if(cnt==0){
                    cnt=1;
                    flag=A[i];
                }
                else{
                    cnt-=1;
                }
            }
        }
        
        if (flag==A[A.Length-1]){
            return flag;
        }
        int flag1=flag;
        int cnt1=0;
        int flag2=A[A.Length-1];
        int cnt2=0;
        foreach(int i in A){
            if(i==flag1){cnt1+=1;}
            if(i==flag2){cnt2+=1;}
        }
        if(cnt1>cnt2){
            return flag1;
        }
        return flag2;
    }
}

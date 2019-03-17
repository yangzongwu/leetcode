public class Solution {
    public int[] SortArrayByParityII(int[] A) {
        int[] result=new int[A.Length];
        int even=1;
        int odd=0;
        foreach(int num in A){
            if(num%2==0){
                result[odd]=num;
                odd+=2;
            }
            else{
                result[even]=num;
                even+=2;
            }
        }
        return result;
    }
}

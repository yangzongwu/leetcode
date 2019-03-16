public class Solution {
    public int[] PlusOne(int[] digits) {
        int flag=1;
        for(int i=digits.Length-1;i>=0;i--){
            int tmp=digits[i]+flag;
            if (tmp>=10){
                flag=1;
                digits[i]=tmp-10;
            }
            else{
                digits[i]=tmp;
                flag=0;
                break;
            }
        }
        
        if (flag==0){
            return digits;
        }
        int[] result=new int[digits.Length+1];
        result[0]=1;
        for (int i=0;i<digits.Length;i++){
            result[i+1]=digits[i];
        }
        return result;
    }
}

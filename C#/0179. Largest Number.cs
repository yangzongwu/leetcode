public class Solution {
    public string LargestNumber(int[] nums) {
        Array.Sort(nums,CompareInt);
        string str="";
        foreach(int num in nums){
            str+=num.ToString();
        }
        if(str[0]=='0')
            return "0";
        return str;
    }
    
    public int CompareInt(int num1,int num2){
        if (Convert.ToInt64(num1.ToString()+num2.ToString())-Convert.ToInt64(num2.ToString()+num1.ToString())>0)
            return -1;
        else
            return 1;
    }
}

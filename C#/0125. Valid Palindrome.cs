public class Solution {
    public bool IsPalindrome(string s) {
        s=s.ToLower();
        IList<char> arr =new List<char>();
        string str="qwertyuiopasdfghjklzxcvbnm1234567890";
        foreach(char ss in s){
            if(str.Contains(ss)){
                arr.Add(ss);
            }
        }
        int left=0;
        int right=arr.Count-1;
        bool result=true;
        while(left<right){
            if(arr[left]!=arr[right]){
                result=false;
                break;
            }
            else{
                left++;
                right--;
            }
        }
        return result;
    }
}

public class Solution {
    public string ReverseOnlyLetters(string S) {
        var tmp=S.ToCharArray();
        string strs="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
        int left=0;
        int right=tmp.Length-1;
        while(left<right){
            while(left<right && !strs.Contains(tmp[left])){
                left++;
            }
            if(left==right){
                break;
            }
            while(right>left && !strs.Contains(tmp[right])){
                right--;
            }
            var tmp1=tmp[left];
            tmp[left]=tmp[right];
            tmp[right]=tmp1;
            left++;
            right--;
        }
        string result= "";
        foreach(char c in tmp){
            result+=c;
        }
        return result;
    }
}

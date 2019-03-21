public class Solution {
    public string ReverseVowels(string s) {
        char[] sList=new char[s.Length];
        sList=s.ToArray();
        int left=0;
        int right=s.Length-1;
        while(left<right){
            while(left<s.Length && !"aouieAOUIE".Contains(sList[left])){
                left++;
            }
            if(left==s.Length){
                break;
            }
            while(!"aouieAOUIE".Contains(sList[right])){
                right--;
            }
            if(left<right){
                char tmp=sList[left];
                sList[left]=sList[right];
                sList[right]=tmp;
                left++;
                right--;
            }            
        }
        string rep="";
        foreach(char c in sList){
            rep=rep+c;
        }
        return rep;
    }
}
//===============================================================================================
public class Solution {
    public string ReverseVowels(string s) {
        string rep1="";
        string rep2="";
        int left=0;
        int right=s.Length-1;
        while(left<=right){
            while(left<right && !"aouieAOUIE".Contains(s[left])){
                rep1=rep1+s[left];
                left++;
            }
            while(right>left && !"aouieAOUIE".Contains(s[right])){
                rep2=s[right]+rep2;
                right--;
            }
            if(left==right){
                rep1=rep1+s[left];
                break;
            }
            else{
                rep1=rep1+s[right];
                rep2=s[left]+rep2;
                left++;
                right--;
            }
        }
        return rep1+rep2;
    }
}
//=====================================================================================
public class Solution {
    public string ReverseVowels(string s) {
        char[] sList=new char[s.Length];
        sList=s.ToArray();
        int left=0;
        int right=s.Length-1;
        while(left<right){
            while(left<s.Length && !"aouieAOUIE".Contains(sList[left])){
                left++;
            }
            if(left==s.Length){
                break;
            }
            while(!"aouieAOUIE".Contains(sList[right])){
                right--;
            }
            if(left<right){
                char tmp=sList[left];
                sList[left]=sList[right];
                sList[right]=tmp;
                left++;
                right--;
            }            
        }
        return new string(sList);
    }
}

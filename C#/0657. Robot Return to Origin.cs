public class Solution {
    public bool JudgeCircle(string moves) {
        int l=0;
        int u=0;
        foreach(char c in moves){
            if(c=='U'){u+=1;}
            else if(c=='D'){u-=1;}
            else if(c=='L'){l+=1;}
            else if(c=='R'){l-=1;}
        }
        return l==0 && u==0;
    }
}

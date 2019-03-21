public class Solution {
    public bool BackspaceCompare(string S, string T) {
        int x=S.Length-1;
        int cntx=0;
        int y=T.Length-1;
        int cnty=0;
        bool flag=true;
        while(x>=0 && y>=0){
            if(S[x]=='#'){
                cntx++;
                x--;
            }
            else if(S[x]!='#' && cntx>0){
                cntx--;
                x--;
            }
            else{
                if(T[y]=='#'){
                    cnty++;
                    y--;
                }
                else if(T[y]!='#' && cnty>0){
                    cnty--;
                    y--;
                }
                else{
                    if(S[x]!=T[y]){
                        flag=false;
                        break;
                    }
                    else{
                        x--;
                        y--;
                    }
                }
            }
        }
        if(flag==false){
            return flag;
        }
        else{
            if(x<0 && y<0){
            return flag;
        }
        else if(x>=0 && y<0){
            return Backspace(S,x,cntx);
        }
        else{//y>=0
            return Backspace(T,y,cnty);
        }
        }       
    }
    public bool Backspace(string S,int loc,int cnt){
        bool rep=true;
        while(loc>=0){
            if(S[loc]=='#'){
                cnt++;
                loc--;
            }
            else if(cnt>0){
                cnt--;
                loc--;
            }
            else{
                rep=false;
                break;
            }
        }
        return rep;
    }
}

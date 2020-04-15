public class Solution {
    public string AddBinary(string a, string b) {
        if(a.Length<b.Length){
            string tmp=a;
            a=b;
            b=tmp;
        }
        int flag='0';
        string rep="";
        for(int i=a.Length-1;i>=0;i--){
            if(i>=a.Length-b.Length){
                if(a[i]=='0' && b[i+b.Length-a.Length]=='0' && flag=='0'){
                    rep='0'+rep;
                }
                else if(a[i]=='1' && b[i+b.Length-a.Length]=='0' && flag=='0'){
                    rep='1'+rep;
                }
                else if(a[i]=='0' && b[i+b.Length-a.Length]=='1' && flag=='0'){
                    rep='1'+rep;
                }
                else if(a[i]=='1' && b[i+b.Length-a.Length]=='1' && flag=='0'){
                    rep='0'+rep;
                    flag='1';
                }else if(a[i]=='0' && b[i+b.Length-a.Length]=='0' && flag=='1'){
                    rep='1'+rep;
                    flag='0';
                }
                else if(a[i]=='1' && b[i+b.Length-a.Length]=='0' && flag=='1'){
                    rep='0'+rep;
                    flag='1';
                }
                else if(a[i]=='0' && b[i+b.Length-a.Length]=='1' && flag=='1'){
                    rep='0'+rep;
                    flag='1';
                }
                else if(a[i]=='1' && b[i+b.Length-a.Length]=='1' && flag=='1'){
                    rep='1'+rep;
                    flag='1';
                }
                
            }
            else{
                if(a[i]=='0' && flag=='0'){
                    rep='0'+rep;
                }
                else if(a[i]=='1' && flag=='0'){
                    rep='1'+rep;
                }
                else if(a[i]=='1' && flag=='1'){
                    rep='0'+rep;
                }
                else{
                    rep='1'+rep;
                    flag='0';
                }
            }
        }
        if (flag=='1'){
            return '1'+rep;
        }
        else{
            return rep;
        }
    }
}

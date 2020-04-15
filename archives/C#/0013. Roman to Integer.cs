public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char,int> dictS=new Dictionary<char,int>();
        dictS.Add('I',1);
        dictS.Add('V',5);
        dictS.Add('X',10);
        dictS.Add('L',50);
        dictS.Add('C',100);
        dictS.Add('D',500);
        dictS.Add('M',1000);
        
        int lenS=s.Length;
        if(lenS==0){
            return 0;
        };
        int rep=dictS[s[lenS-1]];
        for(int i=0;i<lenS-1;i++){
            if(dictS[s[i]]<dictS[s[i+1]]){
                rep-=dictS[s[i]];
            }
            else{
                rep+=dictS[s[i]];
            }
        }
        return rep;
    }
}

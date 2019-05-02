public class Solution {
    public string Convert(string s, int numRows) {
        if(s.Length<numRows ||numRows==1)
            return s;
        string[] strArray=new string[numRows];
        for(int i =0;i<s.Length;i++){
            int k=i%(2*numRows-2);
            if(k<numRows)
                strArray[k]+=s[i];
            else
                strArray[2*numRows-k-2]+=s[i];
        }
        string rep="";
        foreach(var str in strArray){
            rep+=str;
        }
        return rep;
    }
}

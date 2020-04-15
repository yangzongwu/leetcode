public class Solution {
    public string FractionToDecimal(int numerator, int denominator) {
        long num=numerator;
        long den=denominator;
        
        if(num==0)
            return "0";
        if(num%den==0)
            return (num/den).ToString();
        
        int flag=num*den<0?-1:1;
        num=Math.Abs(num);
        den=Math.Abs(den);
        
        string rep= flag==1?"":"-";
        rep+=(num/den).ToString()+".";
        
        num=num%den;
        var numsDict=new Dictionary<long,int>();
        string str="";
        int i=0;
        while(!numsDict.ContainsKey(num) && num!=0){
            numsDict[num]=i;
            i++;
            num=num*10;
            str+=(num/den).ToString();
            num=num%den;
        }
        
        if(num==0)
            rep+=str;
        else{
            int k=numsDict[num];
            for(int j =0;j<k;j++){
                rep+=str[j];
            }
            rep+='(';
            for(int j=k;j<i;j++){
                rep+=str[j];
            }
            rep+=')';
            }
        return rep;
        
    }
}

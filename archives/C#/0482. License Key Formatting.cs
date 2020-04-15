public class Solution {
    public string LicenseKeyFormatting(string S, int K) {
        S=S.Replace("-","");
        S=S.ToUpper();
        if(K>S.Length){
            return S;
        }
        int m=S.Length%K;
        if(m==0){
            return GetLicenseKeyFormatting(S,K);
        }
        else{
            return S.Substring(0,m)+"-"+GetLicenseKeyFormatting(S.Substring(m),K);
        }
    }
    public string GetLicenseKeyFormatting(string S,int K){
        string rep="";
        for(int i=0;i+K-1<S.Length;i+=K){
            rep=rep+"-"+S.Substring(i,K);
        }
        return rep.Substring(1);
    }
}

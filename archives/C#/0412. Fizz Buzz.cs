public class Solution {
    public IList<string> FizzBuzz(int n) {
        IList<string> rep=new List<string>();
        for(int i=1;i<=n;i++){
            if(i%3==0 && i%5==0){
                rep.Add("FizzBuzz");
            }
            else if(i%3==0){
                rep.Add("Fizz");
            }
            else if(i%5==0){
                rep.Add("Buzz");
            }
            else{
                string tmp=Convert.ToString(i);
                rep.Add(tmp);
            }
        }
        return rep;
    }
}

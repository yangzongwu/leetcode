public class Solution {
    public IList<string> LetterCombinations(string digits) {
        var disitsDic=new Dictionary<char,string>();
        disitsDic.Add('2',"abc");
        disitsDic.Add('3',"def");
        disitsDic.Add('4',"ghi");
        disitsDic.Add('5',"jkl");
        disitsDic.Add('6',"mno");
        disitsDic.Add('7',"pqrs");
        disitsDic.Add('8',"tuv");
        disitsDic.Add('9',"wxyz");
        var rep=new List<string>();
        foreach(var c in digits){
            rep=LetterCombinations(disitsDic[c],rep);
        }
        return rep;
        
    }
    public List<string> LetterCombinations(string str,List<string> rep){
        if(rep.Count==0){
            foreach(var c in str){
                rep.Add(c.ToString());
            }
            return rep;
        }
        else{
            List<string> curList=new List<string>();
            foreach(var c in str){
                foreach(var substring in rep){
                    curList.Add(substring+c);
                }
            }
            return curList;
        }
    }
}

public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var result=new List<IList<string>>();
        var rep=new Dictionary<string,List<string>>();
        foreach(var str in strs){
            string sortedStr=SortString(str);
            if(!rep.ContainsKey(sortedStr)){
                rep[sortedStr]=new List<string>{str};
            }
            else{
                rep[sortedStr].Add(str);
            }
        }
        foreach(var k in rep.Keys){
            result.Add(rep[k]);
        }
        return result;
    }
    public string SortString(string str){
        var curList=str.ToCharArray();
        Array.Sort(curList);
        string rep="";
        foreach(var c in curList){
            rep+=c;
        }
        return rep;
    }
}

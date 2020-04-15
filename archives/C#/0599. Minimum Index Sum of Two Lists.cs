public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {
        Dictionary<string,int> list1Dict=new Dictionary<string,int>();
        for(int i=0;i<list1.Count();i++){
            list1Dict[list1[i]]=i;
        }
        IList<string> rep=new List<string>();
        int totalInterest=int.MaxValue;
        
        for(int i=0;i<list2.Count();i++){
            if(list1Dict.ContainsKey(list2[i])){
                if(list1Dict[list2[i]]+i==totalInterest){
                    rep.Add(list2[i]);
                }
                else if(list1Dict[list2[i]]+i<totalInterest){
                    rep.Clear();
                    rep.Add(list2[i]);
                    totalInterest=list1Dict[list2[i]]+i;
                }
            }    
        }
        
        return rep.ToArray();
    }
}

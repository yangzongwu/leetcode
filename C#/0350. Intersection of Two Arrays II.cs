public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        IList<int> rep=new List<int>();
        Dictionary<int,int> numsDict=new Dictionary<int,int>();
        foreach(int num in nums1){
            if(!numsDict.ContainsKey(num)){
                numsDict[num]=1;
            }
            else{
                numsDict[num]+=1;
            }
        }
        foreach(int num in nums2){
            if(numsDict.ContainsKey(num) && numsDict[num]>0){
                numsDict[num]-=1;
                rep.Add(num);
            }
        }
        return rep.ToArray();
    }
}

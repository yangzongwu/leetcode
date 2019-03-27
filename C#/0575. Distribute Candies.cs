public class Solution {
    public int DistributeCandies(int[] candies) {
        HashSet<int> candiesSet=new HashSet<int>();
        foreach(int candy in candies){
            candiesSet.Add(candy);
        }
        return candies.Length/2>candiesSet.Count()?candiesSet.Count():candies.Length/2;
    }
}

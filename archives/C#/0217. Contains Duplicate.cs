using System.Collections.Generic;

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> copynum = new HashSet<int> { };
        foreach(int i in nums)
        {
            copynum.Add(i);
        }
        return copynum.Count != nums.Length;
    }
}

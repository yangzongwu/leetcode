public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        HashSet<int> nums1Set=new HashSet<int>(nums1);
        HashSet<int> nums2Set=new HashSet<int>(nums2);
        nums1Set.IntersectWith(nums2Set);
        result=nums1Set.ToArray();
        return result;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode SortedArrayToBST(int[] nums) {
        int right=nums.Length-1;
        int left=0;
        return subSortedArrayToBST(nums,left,right);
    }
    public TreeNode subSortedArrayToBST(int[] nums,int left,int right){
        if (left>right){
            return null;
        }
        int mid=(left+right)/2;
        TreeNode node=new TreeNode(nums[mid]);
        node.left=subSortedArrayToBST(nums,left,mid-1);
        node.right=subSortedArrayToBST(nums,mid+1,right);
        return node;
        
    }
}

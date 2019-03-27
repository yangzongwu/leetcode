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
    public int LongestUnivaluePath(TreeNode root) {
        if(root==null){
            return 0;
        }
        int maxLongestUnivaluePath=Math.Max(LongestUnivaluePath(root.left),LongestUnivaluePath(root.right));
        int maxSumLongestPath=GetmaxLongestPath(root.left,root.val)+GetmaxLongestPath(root.right,root.val);
        return Math.Max(maxLongestUnivaluePath,maxSumLongestPath);
    }
    
    public int GetmaxLongestPath(TreeNode root,int target){
        if(root==null || root.val!=target){
            return 0;
        }
        return 1+Math.Max(GetmaxLongestPath(root.left,target),GetmaxLongestPath(root.right,target));
    }
}

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
    public bool IsValidBST(TreeNode root) {
        return IsValidBSTFunc(root,(long)int.MinValue-1,(long)int.MaxValue+1);
    }
    
    public bool IsValidBSTFunc(TreeNode root,long minValue,long MaxValue){
        if(root==null){return true;}
        if(root.val<MaxValue && root.val>minValue){
            return IsValidBSTFunc(root.left,minValue,root.val) && IsValidBSTFunc(root.right,root.val,MaxValue);
        }
        return false;
    }
}

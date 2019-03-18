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
    public bool IsUnivalTree(TreeNode root) {
        if (root==null){
            return true;
        }
        int target=root.val;
        return IsSameValue(root,target);
    }
    
    public bool IsSameValue(TreeNode root,int target){
        if(root==null){
            return true;
        }
        if(root.val!=target){
            return false;
        }
        return (IsSameValue(root.right,target) && IsSameValue(root.left,target));
    }
}

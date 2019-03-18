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
    public bool IsBalanced(TreeNode root) {
        if (root==null){
            return true;
        }
        return IsBalanced(root.left) && IsBalanced(root.right) &&(Math.Abs(GetHeight(root.left)-GetHeight(root.right))<=1);
    }
    
    public int GetHeight(TreeNode root){
        if (root==null){
            return 0;
        }
        return 1+Math.Max(GetHeight(root.right),GetHeight(root.left));
    }
}

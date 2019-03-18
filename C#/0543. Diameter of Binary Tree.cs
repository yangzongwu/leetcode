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
    public int DiameterOfBinaryTree(TreeNode root) {
        if (root==null){
            return 0;
        }
        int rep=0;
        rep=Math.Max(rep,DiameterOfBinaryTree(root.left));
        rep=Math.Max(rep,DiameterOfBinaryTree(root.right)); 
        rep=Math.Max(rep,CalHeight(root.left)+CalHeight(root.right));
        return rep;
    }
    
    public int CalHeight(TreeNode root){
        int rep=0;
        if (root==null){
            return rep;
        }
        return 1+Math.Max(CalHeight(root.left),CalHeight(root.right));
    }
}

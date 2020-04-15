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
    public bool IsSymmetric(TreeNode root) {
        if(root==null){
            return true;
        }
        else if((root.left==null && root.right!=null)||(root.left!=null && root.right==null)){
            return false;
        }
        else{
            return SubIsSymmetric(root.left,root.right);
        }
    }
    
    public bool SubIsSymmetric(TreeNode rootA,TreeNode rootB){
        if (rootA==null && rootB==null){
            return true;
        }
        else if ((rootA!=null && rootB==null)||(rootA==null && rootB!=null)){
            return false;
        }
        else{
            if (rootA.val!=rootB.val){
                return false;
            }
            else{
                return SubIsSymmetric(rootA.left,rootB.right) && SubIsSymmetric(rootA.right,rootB.left);
            }
        }
    }
}

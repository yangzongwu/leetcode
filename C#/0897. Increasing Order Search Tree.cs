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
    public TreeNode IncreasingBST(TreeNode root) {
        if(root==null){
            return null;
        }
        TreeNode newroot=new TreeNode(0);
        if(root.left!=null){
            newroot.right=IncreasingBST(root.left);
        }
        TreeNode curRoot=newroot;
        while(curRoot.right!=null){
            curRoot=curRoot.right;
        }
        curRoot.right=root;
        curRoot=curRoot.right;
        curRoot.left=null;
        curRoot.right=IncreasingBST(root.right);
        
        return newroot.right;
            
    }
}

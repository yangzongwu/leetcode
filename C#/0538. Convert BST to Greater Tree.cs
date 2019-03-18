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
    int sum=0;
    public TreeNode ConvertBST(TreeNode root) {
        if (root==null){
            return root;
        }
        ConvertBST(root.right);
        root.val+=sum;
        sum=root.val;
        ConvertBST(root.left);
        return root;
    }
}

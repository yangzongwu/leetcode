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
    public TreeNode TrimBST(TreeNode root, int L, int R) {
        if(root==null){
            return root;
        }
        else if(root.val>R){
            return TrimBST(root.left,L,R);
        }
        else if(root.val<L){
             return TrimBST(root.right,L,R);
        }
        else{
            root.left=TrimBST(root.left,L,R);
            root.right=TrimBST(root.right,L,R);
            return root;
        }
    }
}

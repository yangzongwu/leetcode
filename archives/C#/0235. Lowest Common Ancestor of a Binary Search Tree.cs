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
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val>q.val){
            TreeNode tmp=p;
            p=q;
            q=tmp;
        }
        
        if (p.val==root.val || q.val==root.val){
            return root;
        }
        else if(p.val<=q.val && q.val<root.val){
            return LowestCommonAncestor(root.left,p,q);
        }
        else if(root.val<p.val && p.val<=q.val){
            return LowestCommonAncestor(root.right,p,q);
        }
        else{
            return root;
        }
    }
}

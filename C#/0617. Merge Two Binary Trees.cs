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
    public TreeNode MergeTrees(TreeNode t1, TreeNode t2) {
        if(t1==null && t2==null){
            return t1;
        }    
        else if(t1!=null && t2==null){
            return t1;
        }
        else if(t1==null && t2!=null){
            return t2;
        }
        else{
            t1.val=t1.val+t2.val;
            t1.left=MergeTrees(t1.left,t2.left);
            t1.right=MergeTrees(t1.right,t2.right);
            return t1;
        }
    }
}

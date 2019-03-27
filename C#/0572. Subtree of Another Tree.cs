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
    public bool IsSubtree(TreeNode s, TreeNode t) {
        if(s==null){
            return false;
        }
        return IsSameTree(s,t)||IsSubtree(s.left,t)||IsSubtree(s.right,t);
    }
    public bool IsSameTree(TreeNode s, TreeNode t){
        if(s==null && t==null){return true;}
        else if(s!=null && t==null){return false;}
        else if(s==null && t!=null){return false;}
        else{
            return s.val==t.val?(IsSameTree(s.left,t.left)&&IsSameTree(s.right,t.right)):false;
        }
    }
}

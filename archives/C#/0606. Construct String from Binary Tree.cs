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
    public string Tree2str(TreeNode t) {
        if(t==null){return "";}
        string rep=t.val.ToString();
        if(t.left==null && t.right==null){return rep;}
        else if (t.left!=null && t.right==null){return rep+"("+Tree2str(t.left)+")";}
        else if (t.left==null && t.right!=null){return rep+"()"+"("+Tree2str(t.right)+")";}
        else{return rep+"("+Tree2str(t.left)+")"+"("+Tree2str(t.right)+")";}    
    }
}

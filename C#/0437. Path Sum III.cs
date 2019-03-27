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
    public int PathSum(TreeNode root, int sum) {
        int rep=0;
        if(root==null){
            return 0;
        }
        return NodeToPathSum(root,sum)+PathSum(root.left,sum)+PathSum(root.right,sum);
    }
    
    public int NodeToPathSum(TreeNode root, int sum){
        if(root==null){
            return 0;
        }
        else{
            int rep=0;
            if(sum==root.val){
                rep+=1;
            }
            return rep+NodeToPathSum(root.left,sum-root.val)+NodeToPathSum(root.right,sum-root.val);
            
        }
    }
}

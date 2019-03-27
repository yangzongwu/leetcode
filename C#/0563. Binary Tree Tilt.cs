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
    public int FindTilt(TreeNode root) {
        if(root==null){
            return 0;
        }
        return Math.Abs(CalSumOfVal(root.left)-CalSumOfVal(root.right))+FindTilt(root.left)+FindTilt(root.right);
    }
    public int CalSumOfVal(TreeNode root){
        if(root==null){
            return 0;
        }
        return root.val+CalSumOfVal(root.left)+CalSumOfVal(root.right);
    }
}

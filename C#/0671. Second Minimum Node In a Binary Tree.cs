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
    public int FindSecondMinimumValue(TreeNode root) {
        if(root==null){
            return -1;
        }
        int target=root.val;
        int result=int.MaxValue;
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        rootStack.Push(root);
        while(rootStack.Count()!=0){
            TreeNode curRoot=rootStack.Pop();
            if(curRoot.val!=target){
                result=Math.Min(result,curRoot.val);
            }
            if(curRoot.left!=null){
                rootStack.Push(curRoot.left);
                rootStack.Push(curRoot.right);
            }
        }
        return result==int.MaxValue?-1:result;
    }
}

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
    public int GetMinimumDifference(TreeNode root) {
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        TreeNode node=root;
        int preValue=-1;
        int rep=int.MaxValue;
        while(node!=null || rootStack.Count()!=0){
            while(node!=null){
                rootStack.Push(node);
                node=node.left;
            }
            if(rootStack.Count()!=0){
                TreeNode curNode=rootStack.Pop();
                if(preValue==-1){
                    preValue=curNode.val;
                }
                else{
                    rep=Math.Min(rep,curNode.val-preValue);
                    preValue=curNode.val;
                }
                node=curNode.right;
            }
        }
        return rep;
    }
}

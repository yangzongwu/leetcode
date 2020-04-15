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
    public bool FindTarget(TreeNode root, int k) {
        if(root==null){return false;}
        HashSet<int> rootValSet=new HashSet<int>();
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        rootStack.Push(root);
        while(rootStack.Count()!=0){
            TreeNode curRoot=rootStack.Pop();
            if(rootValSet.Contains(k-curRoot.val)){
                return true;
            }
            rootValSet.Add(curRoot.val);
            if(curRoot.left!=null){
                rootStack.Push(curRoot.left);
            }
            if(curRoot.right!=null){
                rootStack.Push(curRoot.right);
            }
        }
        return false;
    }
}

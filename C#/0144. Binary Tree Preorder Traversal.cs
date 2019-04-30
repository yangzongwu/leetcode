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
    public IList<int> PreorderTraversal(TreeNode root) {
        IList<int> result=new List<int>();
        if(root==null)
            return result;
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        while(root!=null){
            result.Add(root.val);
            if(root.right!=null)
                rootStack.Push(root.right);
            if(root.left!=null)
                root=root.left;
            else if(root.left==null && rootStack.Count()!=0)
                root=rootStack.Pop();
            else
                break;
        }
        return result;
    }
}

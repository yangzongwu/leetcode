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
    public IList<int> InorderTraversal(TreeNode root) {
        IList<int> rep=new List<int>();
        if(root==null){
            return rep;
        }
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        
        while(root!=null || rootStack.Count()>0){
            
            while(root!=null){
                rootStack.Push(root);
                root=root.left;
            }
            root=rootStack.Pop();
            rep.Add(root.val);
            root=root.right;
        }
        return rep;
    }
}

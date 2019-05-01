/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class BSTIterator {
    
    Queue<int> rootQueue=new Queue<int>();
    public BSTIterator(TreeNode root) {
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        while(rootStack.Count()!=0 ||root!=null){
            while(root!=null){
                rootStack.Push(root);
                root=root.left;
            }
            root=rootStack.Pop();
            rootQueue.Enqueue(root.val);
            root=root.right;
        }
    }
        
    /** @return the next smallest number */
    public int Next() {
        return rootQueue.Dequeue();
    }
    
    /** @return whether we have a next smallest number */
    public bool HasNext() {
        return rootQueue.Count()>0;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */

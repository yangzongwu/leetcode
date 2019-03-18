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
    public IList<IList<int>> LevelOrderBottom(TreeNode root) {
        IList<IList<int>> rep= new List<IList<int>>();
        if (root==null){
            return rep;
        }
        
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        while(rootQueue.Count!=0){
            IList<int> cur=new List<int>();
            int lenRootQueue=rootQueue.Count;
            for(int i=0;i<lenRootQueue;i++){
                TreeNode curRoot=rootQueue.Dequeue();
                cur.Add(curRoot.val);
                if (curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                }
                if (curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                }
            }
            rep.Insert(0,cur);
        }
        return rep;
    }
}

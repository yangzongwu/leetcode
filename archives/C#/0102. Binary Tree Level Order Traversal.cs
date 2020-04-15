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
    public IList<IList<int>> LevelOrder(TreeNode root) {
        IList<IList<int>> rep=new List<IList<int>>();
        if(root==null){
            return rep;
        }
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        while(rootQueue.Count()>0){
            int lenRootQueue=rootQueue.Count();
            IList<int> rootList=new List<int>();
            for(int i=0;i<lenRootQueue;i++){
                TreeNode curRoot=rootQueue.Dequeue();
                rootList.Add(curRoot.val);
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                }
            }
            rep.Add(rootList);
        }
        return rep;
    }
}

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
    public IList<int> RightSideView(TreeNode root) {
        var result=new List<int>();
        if(root==null)
            return result;
        var rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        while(rootQueue.Count()!=0){
            int lenRootQueue=rootQueue.Count();
            for(int i=0;i<lenRootQueue;i++){
                var curRoot=rootQueue.Dequeue();
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                }
                if(i==lenRootQueue-1){
                    result.Add(curRoot.val);
                }
            }
        }
        return result;
    }
}

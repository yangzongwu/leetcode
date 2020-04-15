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
    public IList<string> BinaryTreePaths(TreeNode root) {
        IList<string> rep=new List<string>();
        if(root==null){
            return rep;
        }
        Queue<string> strQueue=new Queue<string>();
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        strQueue.Enqueue(root.val.ToString());
        rootQueue.Enqueue(root);
        while(rootQueue.Count()!=0){
            int lenRootQueue=rootQueue.Count();
            for (int i=0;i<lenRootQueue;i++){
                string curString=strQueue.Dequeue();
                TreeNode curRoot=rootQueue.Dequeue();
                if(curRoot.left==null && curRoot.right==null){
                    rep.Add(curString);
                }
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                    strQueue.Enqueue(curString+"->"+curRoot.left.val.ToString());
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                    strQueue.Enqueue(curString+"->"+curRoot.right.val.ToString());
                }
            }
        }
        return rep;
    }
}

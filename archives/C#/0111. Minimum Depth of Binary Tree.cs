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
    public int MinDepth(TreeNode root) {
        if (root==null){
            return 0;
        }
        
        int cnt=0;
        
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        while(rootQueue.Count!=0){
            cnt+=1;
            int lenRootQueue=rootQueue.Count;
            while(lenRootQueue>0){
                lenRootQueue--;
                TreeNode curRoot=rootQueue.Dequeue();
                if(curRoot.left==null && curRoot.right==null){
                    return cnt;
                }
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                }
            }
        }
        return 0;
    }
}

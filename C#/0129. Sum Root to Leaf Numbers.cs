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
    public int SumNumbers(TreeNode root) {
        if(root==null)
            return 0;
        int sum=0;
        var rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        var rootValQueue=new Queue<int>();
        rootValQueue.Enqueue(root.val);
        while(rootQueue.Count()!=0){
            int lenOfRootQueue=rootQueue.Count();
            for(int i=0;i<lenOfRootQueue;i++){
                TreeNode curRoot=rootQueue.Dequeue();
                int curVal=rootValQueue.Dequeue();
                if(curRoot.left==null && curRoot.right==null)
                    sum+=curVal;
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                    rootValQueue.Enqueue(curVal*10+curRoot.left.val);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                    rootValQueue.Enqueue(curVal*10+curRoot.right.val);
                }
            }
        }
        return sum;
    }
}

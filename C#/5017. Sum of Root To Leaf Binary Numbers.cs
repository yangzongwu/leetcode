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
    public int SumRootToLeaf(TreeNode root) {
        if(root==null){
            return 0;
        }
        
        int rep=0;
        
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        Queue<int> sumRootValQueue=new Queue<int>();
        rootQueue.Enqueue(root);
        sumRootValQueue.Enqueue(root.val);
        
        while(rootQueue.Count()!=0){
            int lenOfRootQueue=rootQueue.Count();
            int k=0;
            while(k<lenOfRootQueue){
                TreeNode curRoot=rootQueue.Dequeue();
                int curSumRootVal=sumRootValQueue.Dequeue();
                if(curRoot.left==null && curRoot.right==null){
                    rep=(rep+curSumRootVal)%1000000007;
                }
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                    sumRootValQueue.Enqueue((curRoot.left.val+curSumRootVal*2)%1000000007);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                    sumRootValQueue.Enqueue((curRoot.right.val+curSumRootVal*2)%1000000007);
                }
                k++;
            }
        }
        return rep;
    }
}

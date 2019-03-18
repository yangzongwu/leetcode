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
    public int SumOfLeftLeaves(TreeNode root) {
        if (root==null){
            return 0;
        }    
        int leftSum=0;
        Queue<TreeNode> leftNodeList=new Queue<TreeNode>();
        Queue<TreeNode> rightNodeList=new Queue<TreeNode>();
        rightNodeList.Enqueue(root);
        
        while(leftNodeList.Count!=0 || rightNodeList.Count!=0){
            if (leftNodeList.Count!=0){
                TreeNode curRoot=leftNodeList.Dequeue();
                if (curRoot.left==null && curRoot.right==null){
                    leftSum+=curRoot.val;
                }
                if(curRoot.left!=null){
                    leftNodeList.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rightNodeList.Enqueue(curRoot.right);
                }
            }
            if (rightNodeList.Count!=0){
                TreeNode curRoot=rightNodeList.Dequeue();
                if(curRoot.left!=null){
                    leftNodeList.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rightNodeList.Enqueue(curRoot.right);
                }
            }
        }
        return leftSum;
    }
}

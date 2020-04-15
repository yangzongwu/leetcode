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
    public bool IsCousins(TreeNode root, int x, int y) {
        if(root==null){
            return false;
        }
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        while(rootQueue.Count()!=0){
            bool flag=false;
            int lenOfRootQueue=rootQueue.Count();
            for(int i=0;i<lenOfRootQueue;i++){
                TreeNode curRoot=rootQueue.Dequeue();
                if(curRoot.left!=null && curRoot.right!=null){
                    if(curRoot.left.val==x && curRoot.right.val==y){return false;}
                    if(curRoot.left.val==y && curRoot.right.val==x){return false;}
                }
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                    if((curRoot.left.val==x || curRoot.left.val==y) && flag==false){
                        flag=true;
                    }
                    else if((curRoot.left.val==x ||curRoot.left.val==y) && flag==true){
                        return true;
                    }
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                    if((curRoot.right.val==x ||curRoot.right.val==y) && flag==false){
                        flag=true;
                    }
                    else if((curRoot.right.val==x ||curRoot.right.val==y) && flag==true){
                        return true;
                    }
                }
            }
        }
        return false;
    }
}

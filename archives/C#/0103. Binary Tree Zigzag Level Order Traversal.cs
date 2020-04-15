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
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) {
        IList<IList<int>> rep=new List<IList<int>>();
        if(root==null){return rep;}
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        bool flag=true;
        while(rootQueue.Count()!=0){
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
            if(flag==true){
                rep.Add(rootList);
                flag=false;
            }
            else{
                List<int> tmp=new List<int>(rootList);
                tmp.Reverse();
                IList<int> tmp1=new List<int>(tmp);
                rep.Add(tmp1);
                flag=true;
            }
        }
        return rep;
    }
}

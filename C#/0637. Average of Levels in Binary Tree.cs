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
    public IList<double> AverageOfLevels(TreeNode root) {
        IList<double> rep=new List<double>();
        if(root==null){
            return rep;
        }
        Queue<TreeNode> rootList=new Queue<TreeNode>();
        rootList.Enqueue(root);
        while(rootList.Count!=0){
            List<int> tmp=new List<int>();
            int lenOfRootList=rootList.Count;
            for(int i=0;i<lenOfRootList;i++){
                TreeNode curRoot=rootList.Dequeue();
                tmp.Add(curRoot.val);
                if(curRoot.left!=null){
                    rootList.Enqueue(curRoot.left);
                }
                if(curRoot.right!=null){
                    rootList.Enqueue(curRoot.right);
                }
            }
            rep.Add((double)tmp.Average());
        }
        return rep;
    }
}

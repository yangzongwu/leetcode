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
    public int MaxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        List<TreeNode> root_list= new List<TreeNode>(){root};
        List<TreeNode> newt_list= new List<TreeNode>(){};
        int rep=0;
        while(root_list.Count!=0){
            rep+=1;
            newt_list.Clear();
            foreach(TreeNode curroot in root_list){
                if (curroot.left!=null){
                    newt_list.Add(curroot.left);
                }
                if (curroot.right!=null){
                    newt_list.Add(curroot.right);
                }
            }
            root_list.Clear();
            root_list.AddRange(newt_list);
        }
        return rep;
    }
}
//==========================================================================================
public class Solution {
    public int MaxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        return 1+Math.Max(MaxDepth(root.left),MaxDepth(root.right));
    }
}
//===========================================================================================
public class Solution {
    public int MaxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        
        Queue<TreeNode> rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        int rep=0;
        while(rootQueue.Count!=0){
            rep+=1;
            int lenQueue=rootQueue.Count;
            for(int i=0;i<lenQueue;i++){
                TreeNode node=rootQueue.Dequeue();
                if (node.left!=null){
                    rootQueue.Enqueue(node.left);
                }
                if (node.right!=null){
                    rootQueue.Enqueue(node.right);
                }
            }
        }
        return rep;
        
    }
}

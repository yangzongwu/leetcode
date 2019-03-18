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
    public bool LeafSimilar(TreeNode root1, TreeNode root2) {
        List<int> root1List=new List<int>();
        List<int> root2List=new List<int>();
        root1List=LeafOfRoot(root1);
        root2List=LeafOfRoot(root2);
        if(root1List.Count!=root2List.Count){
            return false;
        }
        for(int i=0;i<root1List.Count;i++){
            if(root1List[i]!=root2List[i]){
                return false;
            }
        }
        return true;
    }
    public List<int> LeafOfRoot(TreeNode root){
        List<int> rep=new List<int>();
        if (root==null){
            return rep;
        }
        
        Stack<TreeNode> rootList=new Stack<TreeNode>();
        rootList.Push(root);
        while(rootList.Count!=0){
            TreeNode curRoot=rootList.Pop();
            if(curRoot.left==null && curRoot.right==null){
                rep.Add(curRoot.val);
            }
            if(curRoot.right!=null){
                rootList.Push(curRoot.right);
            }
            if(curRoot.left!=null){
                rootList.Push(curRoot.left);
            }
            
        }
        return rep;
    }
} 

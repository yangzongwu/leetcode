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
    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        if(preorder.Length==0){
            return null;
        }
        
        int i=0;
        while(inorder[i]!=preorder[0]){
            i++;
        }
        
        int lengthK=preorder.Length;
        TreeNode node=new TreeNode(preorder[0]);
        node.left=BuildTree(CutArray(preorder,1,i),CutArray(inorder,0,i));
        node.right=BuildTree(CutArray(preorder,i+1,lengthK-i-1),CutArray(inorder,i+1,lengthK-i-1));
        return node;
    }
    
    public int[] CutArray(int[] rootorder,int start,int cutLength){
        List<int> rep=new List<int>();
        for(int i=0;i<cutLength;i++){
            rep.Add(rootorder[start+i]);
        }
        return rep.ToArray();
    }
}

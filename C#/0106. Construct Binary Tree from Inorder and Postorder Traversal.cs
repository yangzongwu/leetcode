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
    public TreeNode BuildTree(int[] inorder, int[] postorder) {
        if(inorder.Length==0){
            return null;
        }
        //if(inorder.Length==1){
        //    return new TreeNode(inorder[0]);
        //}
        
        int length=inorder.Length;
        int target=postorder[length-1];
        int i=0;
        
        //Console.WriteLine("{0},{1}",inorder[0],postorder[0]);
        while(inorder[i]!=target){
            i++;
        }
        
        TreeNode node=new TreeNode(target);
        
        List<int> inorderList=new List<int>(inorder);
        List<int> postorderList=new List<int>(postorder);
        node.left=BuildTree(inorderList.GetRange(0,i).ToArray(), postorderList.GetRange(0,i).ToArray());
        
        int[] inorderRight=inorderList.GetRange(i+1,length-1-i).ToArray();
        int[] postorderRight=postorderList.GetRange(i,length-1-i).ToArray();
        node.right=BuildTree(inorderRight,postorderRight);
        return node;
    }
}

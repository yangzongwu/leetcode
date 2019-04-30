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
    public IList<TreeNode> GenerateTrees(int n) {
        return n==0?new List<TreeNode>():GenerateTrees(1,n+1);
    }
    public IList<TreeNode> GenerateTrees(int l,int r){
        IList<TreeNode> result=new List<TreeNode>();
        if(l==r){
            result.Add(null);
            return result;
        }
        for(int m=l;m<r;m++){
            var lList=GenerateTrees(l,m);
            var rList=GenerateTrees(m+1,r);
            foreach(var lNode in lList){
                foreach(var rNode in rList){
                    var node=new TreeNode(m);
                    node.left=lNode;
                    node.right=rNode;
                    result.Add(node);
                }
            }
        }
        return result;
    }
}

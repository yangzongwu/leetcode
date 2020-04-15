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
    public IList<IList<int>> PathSum(TreeNode root, int sum) {
        var result=new List<IList<int>>();
        if(root==null)
            return result;
        var rootQueue=new Queue<TreeNode>();
        rootQueue.Enqueue(root);
        var rootValQueue=new Queue<List<int>>();
        rootValQueue.Enqueue(new List<int>());
        var rootValSumQueue=new Queue<int>();
        rootValSumQueue.Enqueue(0);
        
        while(rootQueue.Count()!=0){
            TreeNode curRoot=rootQueue.Dequeue();
            List<int> curRootValList=rootValQueue.Dequeue();
            int curSum=rootValSumQueue.Dequeue();
            
            curRootValList.Add(curRoot.val);
            curSum+=curRoot.val;
            
            if(curRoot.left==null && curRoot.right==null && curSum==sum){
                result.Add(curRootValList);
            }
            else{
                if(curRoot.left!=null){
                    rootQueue.Enqueue(curRoot.left);
                    var tmp=new List<int>(curRootValList);
                    rootValQueue.Enqueue(tmp);
                    rootValSumQueue.Enqueue(curSum);
                }
                if(curRoot.right!=null){
                    rootQueue.Enqueue(curRoot.right);
                    var tmp=new List<int>(curRootValList);
                    rootValQueue.Enqueue(tmp);
                    rootValSumQueue.Enqueue(curSum);
                }
            }
        }
        return result;
    }
}

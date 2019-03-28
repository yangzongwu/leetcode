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
    public int[] FindMode(TreeNode root) {
        IList<int> result=new List<int>();
        if(root==null){
            return result.ToArray();
        }
        int cnt=0;
        int precnt=0;
        int target=int.MaxValue;
        Stack<TreeNode> rootStack=new Stack<TreeNode>();
        TreeNode node=root;
        while(node!=null || rootStack.Count()!=0){
            while(node!=null){
                rootStack.Push(node);
                node=node.left;
            }
            if(rootStack.Count!=0){
                TreeNode curNode=rootStack.Pop();
                if(target==int.MaxValue){
                    target=curNode.val;
                    cnt=1;
                }
                else if(target==curNode.val){
                    cnt+=1;
                }
                else{
                    if(cnt==precnt){
                        result.Add(target);
                        target=curNode.val;
                        cnt=1;
                    }
                    else if(cnt>precnt){
                        result.Clear();
                        result.Add(target);
                        precnt=cnt;
                        target=curNode.val;
                        cnt=1;
                    }
                    else{
                        target=curNode.val;
                        cnt=1;
                    }
                }
                node=curNode.right;
            }
        }
        if(cnt==precnt){
            result.Add(target);
        }
        if(cnt>precnt){
            result.Clear();
            result.Add(target);
        }
        return result.ToArray();
    }
}

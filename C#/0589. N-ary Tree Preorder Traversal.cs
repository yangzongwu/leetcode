/*
// Definition for a Node.
public class Node {
    public int val;
    public IList<Node> children;

    public Node(){}
    public Node(int _val,IList<Node> _children) {
        val = _val;
        children = _children;
}
*/
public class Solution {
    public IList<int> Preorder(Node root) {
        IList<int> rep=new List<int>();
        if (root==null){
            return rep;
        }
        Stack<Node> nodeStack=new Stack<Node>();
        nodeStack.Push(root);
        while(nodeStack.Count!=0){
            Node curNode=nodeStack.Pop();
            rep.Add(curNode.val);
            for (int i=curNode.children.Count-1;i>=0;i--){
                nodeStack.Push(curNode.children[i]);
            }
        }
        return rep;
    }
}

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
    public int MaxDepth(Node root) {
        if(root==null){
            return 0;
        }
        if (root.children.Count==0){
            return 1;
        }
        int rep=0;
        foreach(Node child in root.children){
            rep=Math.Max(repa,1+MaxDepth(child));
        }
        return rep;
    }
}

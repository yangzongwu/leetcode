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
    public IList<int> Postorder(Node root) {
        IList<int> rep=new List<int>();
        if(root==null){
            return rep;
        }
        Stack<Node> rootList=new Stack<Node>();
        rootList.Push(root);
        
        while (rootList.Count!=0){
            Node curRoot=rootList.Pop();
            rep.Insert(0,curRoot.val);
            foreach(Node child in curRoot.children){
                rootList.Push(child);
            }
        }
        return rep;
    }
}

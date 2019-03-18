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
    public IList<IList<int>> LevelOrder(Node root) {
        IList<IList<int>> rep=new List<IList<int>>();
        if(root==null){
            return rep;
        }
        Queue<Node> rootList=new Queue<Node>();
        rootList.Enqueue(root);
        
        while(rootList.Count!=0){
            IList<int> tmp=new List<int>();
            int lenOfRootList=rootList.Count;
            for(int i=0;i<lenOfRootList;i++){
                Node curRoot=rootList.Dequeue();
                tmp.Add(curRoot.val);
                foreach(Node node in curRoot.children){
                    rootList.Enqueue(node);
                }
            }
            rep.Add(tmp);
        }
        return rep;
    }
}

/*
// Definition for a Node.
public class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node(){}
    public Node(int _val,Node _prev,Node _next,Node _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
}
*/
public class Solution {
    public Node Flatten(Node head) {
        if(head==null){
            return head;
        }
        Stack<Node> rep=new Stack<Node>();
        rep.Push(head);
        
        Node node=new Node(0,null,null,null);
        Node p=node;
        while(rep.Count()!=0){
            Node tmp=rep.Pop();
            tmp.prev=p;
            p.next=tmp;
            p=p.next;
            
            while(p.next!=null || p.child!=null){
                if(p.child!=null){
                    if(p.next!=null){
                        rep.Push(p.next);
                    }
                    p.next=p.child;
                    p.child.prev=p;
                    p.child=null;
                }
                p=p.next;
            }            
        }
        node.next.prev=null;
        return node.next;
    }
}

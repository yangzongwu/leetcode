/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;

    public Node(){}
    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
}
*/
public class Solution {
    public Node CopyRandomList(Node head) {
        if(head==null){
            return head;
        }
        Node node=head;
        while(node!=null){
            Node tmp=node.next;
            Node newnode=new Node(node.val,null,null);
            newnode.next=tmp;
            node.next=newnode;
            node=node.next.next;
        }
        
        Node pNode=head;
        while(pNode!=null){
            if(pNode.random!=null){
                pNode.next.random=pNode.random.next;
            }
            pNode=pNode.next.next;
        }
        
        Node oldNode=head;
        Node newNode=head.next;
        Node pold=oldNode;
        Node pnew=newNode;
        
        while(pnew.next!=null){
            pold.next=pnew.next;
            pold=pold.next;
            pnew.next=pold.next;
            pnew=pnew.next;
        }
        pnew.next=null;
        pold.next=null;
        return newNode;
        
    }
}

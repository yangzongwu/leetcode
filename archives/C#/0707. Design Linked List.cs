/*
["MyLinkedList","addAtHead","addAtIndex","get","get","get"]
[[],[1],[1,2],[1],[0],[2]]
*/
public class ListNode{
    public int val;
    public ListNode next;
    public ListNode(int x){
        val=x;
    }
}

public class MyLinkedList {
    
    public ListNode head;
    public int cnt=0;

    /** Initialize your data structure here. */
    public MyLinkedList() {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int Get(int index) {
        if (index>cnt-1){
            return -1;
        }
        ListNode p=head;
        while(index>0){
            p=p.next;
            index-=1;
        }
        return p.val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void AddAtHead(int val) {
        ListNode newhead=new ListNode(val);
        newhead.next=head;
        cnt+=1;
        head=newhead;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void AddAtTail(int val) {
        ListNode p=head;
        cnt+=1;
        ListNode newnode=new ListNode(val);    
        if (p==null){
             head=newnode;       
        }
        else{
            while(p.next!=null){
            p=p.next;
            }
            p.next=newnode;
        }
        
        
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void AddAtIndex(int index, int val) {
        if(index==0){
            AddAtHead(val);
        }
        else if(index==cnt){
            AddAtTail(val);
        }
        else if(index<cnt){
            ListNode newnode=new ListNode(val);
            cnt+=1;
            
            ListNode node=new ListNode(0);
            node.next=head;
            ListNode p=node;
            while (index>0){
                p=p.next;
                index-=1;
            }
            newnode.next=p.next;
            p.next=newnode;
            }
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void DeleteAtIndex(int index) {
        if (cnt>0 && index<cnt){
            cnt-=1;
        
            ListNode node=new ListNode(0);
            node.next=head;
            ListNode p=node;
            while (index>0){
                p=p.next;
                index-=1;
            }
            p.next=p.next.next;
    }
}
}
/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */

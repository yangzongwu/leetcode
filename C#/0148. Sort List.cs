/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode SortList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode pfast=head;
        ListNode pslow=head;
        while(pfast.next!=null && pfast.next.next!=null){
            pslow=pslow.next;
            pfast=pfast.next.next;
        }
        
        ListNode pSecond=SortList(pslow.next);
        pslow.next=null;
        ListNode pFirst=SortList(head);
        
        return mergeTwoSortedList(pFirst,pSecond);
    }
    
    public ListNode mergeTwoSortedList(ListNode l1,ListNode l2){
        ListNode node=new ListNode(0);
        ListNode p=node;
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                p.next=l1;
                p=p.next;
                l1=l1.next;
            }
            else{
                p.next=l2;
                p=p.next;
                l2=l2.next;
            }
        }
        if(l1!=null){p.next=l1;}
        if(l2!=null){p.next=l2;}
        
        return node.next;
    }
}

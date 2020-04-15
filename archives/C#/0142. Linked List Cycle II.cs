/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode DetectCycle(ListNode head) {
        if(head==null || head.next==null){
            return null;
        }
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode pslow=node.next;
        ListNode pfast=node.next.next;
        while(pfast.next!=null && pfast.next.next!=null && pslow!=pfast){
            pslow=pslow.next;
            pfast=pfast.next.next;
        }
        if(pfast.next==null || pfast.next.next==null){
            return null;
        }
        
        
        ListNode p=node;
        while(p!=pslow){
            p=p.next;
            pslow=pslow.next;
        }
        return pslow;
    }
}

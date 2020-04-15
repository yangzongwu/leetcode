/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode p=node;
        if(p.next.val==p.next.next.val){
            while(p.next!=null && p.next.next!=null && p.next.val==p.next.next.val){
                p.next=p.next.next;
            }
            p.next=DeleteDuplicates(p.next.next);
        }
        else{
            p=p.next;
            p.next=DeleteDuplicates(p.next);
        }
        return node.next;
    }
}

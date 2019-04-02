/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode OddEvenList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode pOdd=head;
        ListNode pEvenPart=head.next;
        ListNode pEven=pEvenPart;
        while (pEven.next!=null && pEven.next.next!=null){
            pOdd.next=pEven.next;
            pOdd=pOdd.next;
            pEven.next=pOdd.next;
            pEven=pEven.next;
        }
        if(pEven.next!=null){
            pOdd.next=pEven.next;
            pOdd=pOdd.next;
        }
        pEven.next=null;
        pOdd.next=pEvenPart;
        return head;
    }
}

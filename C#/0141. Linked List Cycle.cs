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
    public bool HasCycle(ListNode head) {
        if (head==null || head.next==null){
            return false;
        }
        ListNode pslow=head;
        ListNode pfast=head;
        while(pfast.next!=null && pfast.next.next!=null){
            pslow=pslow.next;
            pfast=pfast.next.next;
            if (pslow==pfast){
                return true;
            }
        }
        return false;
    }
}

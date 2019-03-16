/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MiddleNode(ListNode head) {
        //012345  1-2    2-4
        //01234  1-2 2-4
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode pslow=node;
        ListNode pfast=node;
        while(pfast.next!=null && pfast.next.next!=null){
            pslow=pslow.next;
            pfast=pfast.next.next;
        }
        return pslow.next;
        
    }
}

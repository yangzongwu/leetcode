/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode p=node;
        while(p.next!=null && p.next.next!=null){
            ListNode preSecond=p.next.next;
            ListNode preFirst=p.next;
            preFirst.next=preSecond.next;
            p.next=preSecond;
            preSecond.next=preFirst;
            p=p.next.next;
        }
        return node.next;
    }
}

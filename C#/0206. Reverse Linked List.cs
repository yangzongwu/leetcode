/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        ListNode prev= null;
        while(head!=null){
            ListNode cur=head;
            head=head.next;
            cur.next=prev;
            prev=cur;
        }
        return prev;
    }
}

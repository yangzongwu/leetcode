/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode DeleteDuplicates(ListNode head)
        {
            ListNode node = new ListNode(0);
            node.next = head;
            ListNode p = node;
            while (p.next!=null && p.next.next != null)
            {
                if (p.next.val == p.next.next.val)
                {
                    p.next = p.next.next;
                }
                else
                {
                    p = p.next;
                }
            }
            return node.next;

        }
}

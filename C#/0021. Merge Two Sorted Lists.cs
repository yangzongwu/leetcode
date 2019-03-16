/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2)
        {
            if (l1 == null)
            {
                return l2;
            }
            if (l2 == null)
            {
                return l1;
            }
            ListNode newhead = new ListNode(0);
            ListNode p = newhead;
            while(l1!=null && l2 != null)
            {
                if (l1.val <= l2.val)
                {
                    p.next = l1;
                    p = p.next;
                    l1 = l1.next;
                }
                else
                {
                    p.next = l2;
                    l2 = l2.next;
                    p = p.next;
                }
            }
            if (l1!=null)
            {
                p.next = l1;
            }
            if (l2 != null)
            {
                p.next = l2;
            }
            return newhead.next;
        }

}

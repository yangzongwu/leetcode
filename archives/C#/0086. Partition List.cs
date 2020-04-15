/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode Partition(ListNode head, int x) {
        ListNode smallNode=new ListNode(0);
        ListNode largerNode=new ListNode(0);
        ListNode pSmall=smallNode;
        ListNode pLarger=largerNode;
        while(head!=null){
            if(head.val>=x){
                pLarger.next=head;
                pLarger=pLarger.next;
                head=head.next;
            }
            else{
                pSmall.next=head;
                pSmall=pSmall.next;
                head=head.next;   
            }
        }
        pLarger.next=null;
        pSmall.next=largerNode.next;
        return smallNode.next;
    }
}

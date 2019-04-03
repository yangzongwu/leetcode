/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode InsertionSortList(ListNode head) {
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode p=node;
        while(p.next!=null && p.next.next!=null){
            if(p.next.val<=p.next.next.val){
                p=p.next;
            }
            else{
                ListNode cur=p.next.next;
                p.next.next=cur.next;
                
                ListNode tmp=node;
                while(tmp.next.val<cur.val){
                    tmp=tmp.next;
                }
                cur.next=tmp.next;
                tmp.next=cur;
            }
        }
        return node.next;
    }
}

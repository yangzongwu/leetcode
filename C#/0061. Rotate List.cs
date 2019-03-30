/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode RotateRight(ListNode head, int k) {
        if(k==0 || head==null){
            return head;
        }
        ListNode p=head;
        int cnt=0;
        while(p!=null){
            p=p.next;
            cnt++;
        }
        k=k%cnt;
        if(k==0){
            return head;
        }
        
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode p1=node;
        int keepLenth=cnt-k;
        while(keepLenth>0){
            p1=p1.next;
            keepLenth--;
        }
        ListNode newhead=p1.next;
        p1.next=null;
        
        ListNode pNewHead=newhead;
        while(pNewHead.next!=null){
            pNewHead=pNewHead.next;
        }
        pNewHead.next=head;
        return newhead;
    }
}

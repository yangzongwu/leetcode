/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode ReverseBetween(ListNode head, int m, int n) {
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode p=node;
        while(m-1>0){
            p=p.next;
            m--;
            n--;
        }
        p.next=ReverseFirstN(p.next,n);
        return node.next;
    }
    public ListNode ReverseFirstN(ListNode head,int n){
        ListNode p=head;
        int m=n;
        while(m>1){
            p=p.next;
            m--;
        }
        
        ListNode prev=p.next;
        p.next=null;
        ListNode cur;
        
        while(n>0){
            n--;
            cur=head;
            head=head.next;
            cur.next=prev;
            prev=cur;
        }
        return prev;
    }
}

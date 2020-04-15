/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void ReorderList(ListNode head) {
        if(head!=null){
            ListNode pSlow=head;
            ListNode pFast=head;
            while(pFast.next!=null && pFast.next.next!=null){
                pSlow=pSlow.next;
                pFast=pFast.next.next;
            }
        
            ListNode pSecond=ReverseList(pSlow.next);
            pSlow.next=null;
            ListNode pFirst=head;
        
            ListNode newNode=new ListNode(0);
            ListNode p=newNode;
            while (pSecond!=null){
                p.next=pFirst;
                pFirst=pFirst.next;
                p=p.next;
                p.next=pSecond;
                pSecond=pSecond.next;
                p=p.next;
            }
            if(pFirst!=null){
                p.next=pFirst;
            }
        
            //return newNode.next;
        }
        
    }
    
    public ListNode ReverseList(ListNode head){
        ListNode prev=null;
        while(head!=null){
            ListNode cur=head;
            head=head.next;
            cur.next=prev;
            prev=cur;
        }
        return prev;
        
    }
}

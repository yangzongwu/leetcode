/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public bool IsPalindrome(ListNode head) {
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode pslow=node;
        ListNode pfast=node;
        while (pfast.next!=null && pfast.next.next!=null){
            pslow=pslow.next;
            pfast=pfast.next.next;
        }
        ListNode newhead;
        if(pfast.next!=null){
            newhead=pslow.next.next;
        }
        else{
            newhead=pslow.next;
        }
        
        //reverse linked list
        Solution rep=new Solution();
        newhead=rep.reverseList(newhead);
        
        //compare
        while(newhead!=null){
            if(newhead.val!=head.val){
                return false;
            }
            else{
                newhead=newhead.next;
                head=head.next;
            }
        }
        return true;
        
    }
    
    public ListNode reverseList(ListNode head){
        ListNode prev=null;
        while (head!=null){
            ListNode cur=head;
            head=head.next;
            cur.next=prev;
            prev=cur;
        }
        return prev;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node=new ListNode(0);
        ListNode p=node;
        int flag=0;
        while(l1!=null && l2!=null){
            if(l1.val+l2.val+flag>=10){
                p.next=new ListNode(l1.val+l2.val+flag-10);
                flag=1;
                p=p.next;
                l1=l1.next;
                l2=l2.next;
            }
            else{
                p.next=new ListNode(l1.val+l2.val+flag);
                flag=0;
                p=p.next;
                l1=l1.next;
                l2=l2.next;
            }
        }
        while(l1!=null){
            if(l1.val+flag>=10){
                p.next=new ListNode(l1.val+flag-10);
                flag=1;
                p=p.next;
                l1=l1.next;
            }
            else{
                p.next=new ListNode(l1.val+flag);
                flag=0;
                p=p.next;
                l1=l1.next;
                p.next=l1;
                break;
            }
        }
        while(l2!=null){
            if(l2.val+flag>=10){
                p.next=new ListNode(l2.val+flag-10);
                flag=1;
                p=p.next;
                l2=l2.next;
            }
            else{
                p.next=new ListNode(l2.val+flag);
                flag=0;
                p=p.next;
                l2=l2.next;
                p.next=l2;
                break;
            }
        }
        if(flag==1){
            p.next=new ListNode(1);
        }
        return node.next;
    }
}

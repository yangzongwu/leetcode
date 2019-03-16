/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA=headA;
        ListNode pB=headB;
        
        while (pA!=null && pB!=null){
            pA=pA.next;
            pB=pB.next;    
        }
        if (pB!=null){
            while(pB!=null){
                pB=pB.next;
                headB=headB.next;
            }
            while(headA!=headB){
                headA=headA.next;
                headB=headB.next;
            }
            return headB;
        }
        else if(pA!=null){
            while(pA!=null){
                pA=pA.next;
                headA=headA.next;
            }
            while(headA!=headB){
                headA=headA.next;
                headB=headB.next;
            }
            return headA;
        }
        else{
            while(headA!=headB){
                headA=headA.next;
                headB=headB.next;
            }
            return headA;
        }
        
        
    }
}

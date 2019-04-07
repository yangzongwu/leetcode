/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int[] NextLargerNodes(ListNode head) {
        List<int> result=new List<int>();
        ListNode p;
        while(head!=null){
            p=head.next;
            int target=head.val;
            while(p!=null && p.val<=target){
                p=p.next;
            }
            if(p==null){
                result.Add(0);
            }
            else{
                result.Add(p.val);
            }
            head=head.next;
        }
        return result.ToArray();
    }
}

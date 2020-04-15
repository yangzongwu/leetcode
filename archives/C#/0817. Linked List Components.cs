/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int NumComponents(ListNode head, int[] G) {
        HashSet<int> GSet=new HashSet<int>(G);
        int cnt=0;
        bool flag=false;
        while(head!=null){
            if(GSet.Contains(head.val) && flag==false){
                cnt++;
                flag=true;   
            }
            else if(!GSet.Contains(head.val)){
                flag=false;
            }
            head=head.next;
        }
        return cnt;
    }
}

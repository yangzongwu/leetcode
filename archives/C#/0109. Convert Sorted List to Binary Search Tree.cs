/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode SortedListToBST(ListNode head) {
        if(head==null){
            return null;
        }
        if(head.next==null){
            return new TreeNode(head.val);
        }
        ListNode node=new ListNode(0);
        node.next=head;
        ListNode pslow=node;
        ListNode pfast=node;
        while(pfast.next!=null && pfast.next.next!=null){
            pslow=pslow.next;
            pfast=pfast.next.next;
        }
        TreeNode treeNode=new TreeNode(pslow.next.val);
        treeNode.right=SortedListToBST(pslow.next.next);
        pslow.next=null;
        treeNode.left=SortedListToBST(head);
        return treeNode;
        
    }
}

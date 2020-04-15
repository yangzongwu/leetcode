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
        Stack<int> l1Stack = new Stack<int>();
        Stack<int> l2Stack = new Stack<int>();
        Stack<int> rep = new Stack<int>();
        ListNode result=new ListNode(0);
        ListNode p=result;
        while(l1!=null){
            l1Stack.Push(l1.val);
            l1=l1.next;
        }
        while(l2!=null){
            l2Stack.Push(l2.val);
            l2=l2.next;
        }
        int flag=0;
        while(l1Stack.Count!=0 && l2Stack.Count!=0){
            int sum=flag+l1Stack.Pop()+l2Stack.Pop();
            if(sum>=10){
                flag=1;
                rep.Push(sum-10);
            }
            else{
                flag=0;
                rep.Push(sum);
            }
        }
        while(l1Stack.Count!=0){
            int sum=flag+l1Stack.Pop();
            if(sum>=10){
                flag=1;
                rep.Push(sum-10);
            }
            else{
                flag=0;
                rep.Push(sum);
            }
        }
        while(l2Stack.Count!=0){
            int sum=flag+l2Stack.Pop();
            if(sum>=10){
                flag=1;
                rep.Push(sum-10);
            }
            else{
                flag=0;
                rep.Push(sum);
            }
        }
        if(flag==1){
            rep.Push(1);
        }
        while(rep.Count!=0){
            p.next=new ListNode(rep.Pop());
            p=p.next;
        }
        return result.next;
    }
}

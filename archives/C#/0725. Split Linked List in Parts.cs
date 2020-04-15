/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode[] SplitListToParts(ListNode root, int k) {
        int rootLength=CalListLength(root);
        int k1=rootLength/k;//0
        int k2=rootLength%k;//3
        
        List<ListNode> result=new List<ListNode>();
        for(int i=0;i<k2;i++){
            ListNode[] rep=splitFirstKList(root,k1+1);
            root=rep[1];
            result.Add(rep[0]);
        }
        
       
        for(int i=0;i<k-k2;i++){
            ListNode[] rep1=splitFirstKList(root,k1);
            root=rep1[1];
            result.Add(rep1[0]);
        }
        return result.ToArray();
    }
    
    public int CalListLength(ListNode root){
        int cnt=0;
        while(root!=null){
            cnt++;
            root=root.next;
        }
        return cnt;
    }
    
    public ListNode[] splitFirstKList(ListNode root,int k){
        ListNode[] rep=new ListNode[]{null,null};
        if(root==null || k==0){
            return rep;
        }
        ListNode p=new ListNode(0);
        p.next=root;
        ListNode tmp=p;
        while(k>0){
            tmp=tmp.next;
            k--;
        }
        rep[1]=tmp.next;
        tmp.next=null;
        rep[0]=p.next;
        return rep;
    }
}
